# app.py
from fastapi import FastAPI, WebSocket
import asyncio
import subprocess

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected.")

    try:
        while True:
            data = await websocket.receive_text()
            if "start_interview" in data:
                # Launch the LiveKit voice assistant in subprocess
                process = await asyncio.create_subprocess_exec(
                    "python3", "main.py", "console",
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.STDOUT
                )
                await websocket.send_text("Interview started (LLM backend running).")
    except Exception as e:
        print("WebSocket error:", e)
    finally:
        await websocket.close()
        print("Client disconnected.")