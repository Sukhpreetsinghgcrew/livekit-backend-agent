FROM public.ecr.aws/ubuntu/ubuntu:22.04_stable
ENV DEBIAN_FRONTEND=noninteractive

RUN  apt-get update && \
     apt-get install -y python3 python3-pip && \
     apt-get clean && rm -rf /var/lib/apt/lists/*
     
     
WORKDIR /app

RUN pip3 install --no-cache-dir \
    flask flask-cors python-dotenv livekit-api

COPY server.py .
EXPOSE 5001

CMD ["python3","server.py"]