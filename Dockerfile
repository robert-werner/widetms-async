FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

RUN apt update
RUN apt install -y libjemalloc-dev
COPY . .
RUN pip install -r ./requirements.txt
ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so