import pvporcupine
from dotenv import load_dotenv
import os

# =========================================================== ACCESS KEYS AND KEYWORD PATHS ===========================================================

# Porcupine Access Key and Keyword Path
load_dotenv()
ACCESS_KEY = os.getenv("ACCESS_KEY")    
KEYWORD_PATH = os.getenv("CONTEXT_PATH_PN") 

# =========================================================== HELPER FUNCTION ===========================================================
def listen_for_wake(porcupine, device_index=0):
    from pvrecorder import PvRecorder
    recorder = PvRecorder(device_index=device_index, frame_length=porcupine.frame_length)
    recorder.start()
    try:
        while True:
            pcm = recorder.read()
            if porcupine.process(pcm) >= 0:
                print("Wake word detected!")
                return True  # signal wake word
    finally:
        recorder.stop()
        recorder.delete()

def speak(message):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

# =========================================================== MAIN FUNCTION ===========================================================

def main():
    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keyword_paths=[KEYWORD_PATH]
    )

    print("Listening for wake word...")
    try:
        while True:
            if listen_for_wake(porcupine):
                speak("Yes?")
                return True  # signal to proceed to intent parsing
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        porcupine.delete()

if __name__ == "__main__":
    main()