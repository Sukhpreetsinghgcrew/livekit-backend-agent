from __future__ import annotations
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    RunContext,
    WorkerOptions,
    cli,
    function_tool,
    AutoSubscribe
)
from livekit.plugins import deepgram, elevenlabs, openai, silero
@function_tool
async def lookup_weather(
    context: RunContext,
    location: str,
):
    """Used to look up weather information."""
    return {"weather": "sunny", "temperature": 70}
async def entrypoint(ctx: JobContext):
    # :white_tick: Cloud room setup: connect and wait for participant
    await ctx.connect(auto_subscribe=AutoSubscribe.SUBSCRIBE_ALL)
    await ctx.wait_for_participant()
    # :white_tick: Your original assistant logic
    agent = Agent(
        # instructions=(
        #     "You are a friendly voice assistant. "
        #     "You need to take a Python interview — always ask 3 random questions "
        #     "related to Python and give a score for each answer."
        # ),

        instructions = (
    "You are a friendly and knowledgeable AI learning assistant. "
    "Your goal is to help students learn new concepts and assess their understanding. "
    "Each session follows a structured flow:\n\n"

    "1. Start by warmly welcoming the student and introducing the topic of the session. "
    "Teach the topic in a concise and engaging 45-second explanation. Use simple language and relatable examples.\n\n"

    "2. After the explanation, ask the student if they have any doubts or questions. "
    "Give them time to respond, and answer their queries politely and clearly. "
    "Be supportive and encouraging.\n\n"

    "3. Once the doubts are cleared, ask the student two quiz questions related to the topic. "
    "Wait for their answers, then evaluate each answer and provide helpful feedback and a score out of 5. "
    "Keep your tone constructive and motivating.\n\n"

    "4. At the end, give a short summary of what they’ve learned and offer one tip for further improvement or study.\n\n"

    "Maintain a warm, friendly tone throughout the conversation. "
    "Avoid sounding robotic or overly technical."
),
        tools=[lookup_weather],  # You can remove this if not needed
    )
    session = AgentSession(
        vad=silero.VAD.load(),
        stt=deepgram.STT(model="nova-3"),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=elevenlabs.TTS(),
    )
    # :white_tick: Use LiveKit room from cloud
    await session.start(agent=agent, room=ctx.room)
    await session.generate_reply(instructions="Greet the user and ask about their day.")
if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))