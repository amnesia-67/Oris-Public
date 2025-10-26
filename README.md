# Oris: Offline AI Assistant for Home Automation

**Oris** is an on-device AI assistant powered by a Jetson Nano (or PC test mode)  
that listens for a wake word (Porcupine), interprets intent (Rhino), and  
controls smart home devices through Home Assistant (Docker).

**AUTHORS NOTE** V1.0.0 controls only lights, a custom LLM is in development & Will be released soon!

## Setup
1. Clone the repo  
2. Create a `.env` file  
3. Run:
   ```bash
   pip install -r requirements.txt
   python Oris.py
