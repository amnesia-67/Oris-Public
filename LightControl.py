import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
HA_URL = os.getenv("HA_URL")
TOKEN = os.getenv("HA_TOKEN")
LIGHT_ENTITY = os.getenv("LIGHT_ENTITY")

def ha_request(service, data):
    """Send a POST request to Home Assistant REST API."""
    url = f"{HA_URL}/api/services/{service}"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }
    r = requests.post(url, headers=headers, json=data)
    if not r.ok:
        print(f"[!] Error {r.status_code}: {r.text}")
    return r

def turn_on_light(entity_id=LIGHT_ENTITY):
    print(f"[+] Turning ON {entity_id}")
    ha_request("light/turn_on", {"entity_id": entity_id})

def turn_off_light(entity_id=LIGHT_ENTITY):
    print(f"[+] Turning OFF {entity_id}")
    ha_request("light/turn_off", {"entity_id": entity_id})

def main():
    print("[*] Testing Home Assistant connection...")
    turn_on_light(LIGHT_ENTITY)
    time.sleep(5)
    turn_off_light(LIGHT_ENTITY)
    print("[+] Test complete.")

if __name__ == "__main__":
    main()
