FROM python:3.9.5-slim

COPY . .
RUN apt update
RUN apt install -y libjemalloc-dev
EXPOSE 8000
CMD ["LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so", "python", "main.py"]