import pvrhino
from pvrecorder import PvRecorder
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# =========================================================== ACCESS KEYS AND CONTEXT PATHS ===========================================================
ACCESS_KEY = os.getenv("ACCESS_KEY")
CONTEXT_PATH =  os.getenv("CONTEXT_PATH_RH")

def main():
    start_time = time.time()
    rhino = pvrhino.create(
        access_key=ACCESS_KEY,
        context_path=CONTEXT_PATH
    )

    recorder = PvRecorder(device_index=0, frame_length=rhino.frame_length)
    recorder.start()

    print("Speak a command (Ctrl+C to stop)...")

    try:
        while True:
            if time.time() - start_time > 5:
                print("Timeout reached, stopping...")
                break
            pcm = recorder.read()
            if rhino.process(pcm):  # True → inference finalized
                inference = rhino.get_inference()
                if inference.is_understood:
                    print(f"Intent: {inference.intent}")
                    print(f"Slots: {inference.slots}")
                    return inference.intent
                else:
                    print("Didn't understand.")
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        recorder.stop()
        recorder.delete()
        rhino.delete()

if __name__ == "__main__":
    main() 