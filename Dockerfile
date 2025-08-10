FROM public.ecr.aws/ubuntu/ubuntu:22.04_stable

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Added "elevenlabs" to the extras list
RUN pip3 install --no-cache-dir \
    "livekit-agents[openai,silero,deepgram,cartesia,turn-detector,elevenlabs]~=1.0"

COPY . .

CMD ["python3", "main.py", "dev"]
