# app.py
import os
import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS
from livekit import api
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# LIVEKIT_API_KEY = "APIR24Z2cXf9sJZ"
# LIVEKIT_API_SECRET = "fxHSH2xYeYYYVc9uiuY1gGkudsNhfzt1Lm27xcQzeewG"

LIVEKIT_API_KEY="API7GYmACUohuD2"
LIVEKIT_API_SECRET="x8ouzeDm2oVEPzcGs2EFqpp80ZAPIiT1z2bx1zAVolY"

#LIVEKIT_API_KEY="devkey"
#LIVEKIT_API_SECRET="secret"


@app.route('/get-token', methods=['GET'])
def get_token():
    identity = request.args.get("identity", f"user-{uuid.uuid4().hex[:6]}")
    room = request.args.get("room", f"room-{uuid.uuid4().hex[:6]}")
    print(f"Generating token for room: {room}, identity: {identity}")

    token = api.AccessToken(LIVEKIT_API_KEY, LIVEKIT_API_SECRET)\
        .with_identity(identity)\
        .with_name(identity)\
        .with_grants(api.VideoGrants(
            room_join=True,
            room=room,
            can_publish=True,
            can_subscribe=True
        ))

    jwt = token.to_jwt()
    return jsonify({
        "token": jwt,
        "room": room,
        "identity": identity
    })

if __name__ == "__main__":
    app.run(port=5001, debug=True)
