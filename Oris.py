import time

# Local imports
from WakeWord import main as wk
from IntentParser import main as ip
from LightControl import turn_on_light, turn_off_light

while True:
    try:
        if wk():
            intent = ip()
            if intent == "TurnLightsOn":
                turn_on_light()
            elif intent == "TurnLightsOff":
                turn_off_light()

    except KeyboardInterrupt:
        print("Exiting...")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(1)  # brief pause before restarting loop
        continue