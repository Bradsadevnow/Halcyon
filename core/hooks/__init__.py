from dataclasses import dataclass
from typing import Any, Callable, Dict, List

@dataclass(frozen=True)\nclass GameEvent:
    name: str
    payload: Dict[str, Any]
    t: int

class EventBus:
    def __init__(self):
        self._subs: Dict[str, List[Callable[[GameEvent], None]]] = {}
        self._t = 0
    def dispatch(self, name: str, **payload):
        self._t += 1
        evt = GameEvent(name, payload, self._t)
        for fn in self._subs.get(name, []):
            fn(evt)
        for fn in self._subs.get("*", []):
            fn(evt)
        return evt
    def subscribe(self, name: str, handler: Callable[[GameEvent], None]):
        self._subs.setdefault(name, []).append(handler)