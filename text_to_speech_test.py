import requests

# === Configuration ===
API_KEY = "sk_12b5e0e355d0150cdc6d41fe0545e1ebf867e660dd4eecb8"  # <-- Replace with your real ElevenLabs API key
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Default voice (Rachel)

TEXT = "Hello! This is a test using Eleven Labs Text to Speech API."

# === Make the API call ===
url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

headers = {
    "Accept": "audio/mpeg",
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "text": TEXT,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75
    }
}

print("Sending request to ElevenLabs...")
response = requests.post(url, headers=headers, json=data)

# === Save the audio file ===
if response.status_code == 200:
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    print("✅ Audio saved to output.mp3")
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)
