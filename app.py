# app.py
import os
import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from main import run_interview

load_dotenv()

app = FastAPI()

@app.get("/")
async def get():
    with open("index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected.")
    await websocket.send_text("🟢 Starting interview...")

    try:
        await run_interview(websocket)
    except Exception as e:
        await websocket.send_text(f" Error: {e}")
    finally:
        await websocket.close()
        print("Client disconnected.")
