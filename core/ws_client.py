
# ws_client.py
# Minimal WebSocket emitter to forward GUI packets to the HUD server.
# Usage:
#   from ws_client import make_ws_emitter
#   thalamus.gui.on("heartbeat",  make_ws_emitter())
#   thalamus.gui.on("trace_step", make_ws_emitter())
#
# This will best-effort connect and send JSON strings to ws://127.0.0.1:8765

import asyncio, json, threading
try:
    import websockets
except Exception as e:
    websockets = None

class _WSForwarder:
    def __init__(self, url='ws://127.0.0.1:8765'):
        self.url = url
        self._loop = None
        self._ws = None
        self._thread = None
        self._queue = asyncio.Queue()

    def start(self):
        if self._thread: return
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def _run_loop(self):
        asyncio.run(self._main())

    async def _connect(self):
        if websockets is None:
            return None
        try:
            ws = await websockets.connect(self.url, ping_interval=20, ping_timeout=20)
            return ws
        except Exception:
            return None

    async def _main(self):
        if websockets is None:
            return
        while True:
            if self._ws is None:
                self._ws = await self._connect()
                if self._ws is None:
                    await asyncio.sleep(1.0)
                    continue
            try:
                msg = await self._queue.get()
                await self._ws.send(msg)
            except Exception:
                try:
                    await self._ws.close()
                except Exception:
                    pass
                self._ws = None
                await asyncio.sleep(0.5)

    def emit(self, payload: dict):
        # Ensure background started
        self.start()
        try:
            msg = json.dumps(payload, ensure_ascii=False)
        except Exception:
            msg = json.dumps({"_bad_payload": True})
        # Put without awaiting (thread-safe via loop running in same thread)
        # We use asyncio.Queue; put_nowait is fine here.
        try:
            self._queue.put_nowait(msg)
        except Exception:
            pass

def make_ws_emitter(url='ws://127.0.0.1:8765'):
    fw = _WSForwarder(url=url)
    def _emit(pkt):
        fw.emit(pkt)
    return _emit
