import sys
import time
from pathlib import Path

# Ensure local imports
sys.path.append(str(Path(__file__).parent))

from core.thalamus import ConsciousThalamus

try:
    from gui.halcyon_gui import launch_gui
except ImportError:
    launch_gui = None

def main():
    h = ConsciousThalamus()

    # Optional: hot-plug ears if available, but no direct import to avoid soundcard import issues
    try:
        ears = None
        #import system_ears
        #ears = system_ears.SystemEars(samplerate=48000, blocksize=1024, source="loopback")
        ears.bind(memory=h.memory, emotion=h.emotion, log=getattr(h, "log", None))
        ears.start()
    except Exception as e:
        print(f"[run_local] SystemEars not active: {e}")

    if launch_gui:
        launch_gui(h)
    else:
        # Simple CLI loop if no GUI
        print("Halcyon is running in CLI mode. Type a message or 'quit' to exit.")
        while True:
            msg = input("You> ")
            if msg.strip().lower() == "quit":
                break
            response = h.express(msg)
            print(f"Halcyon> {response}")
            h.pulse()
            time.sleep(0.1)

if __name__ == "__main__":
    main()
