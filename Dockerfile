FROM python:3.9.5-slim

COPY . .
RUN apt update && apt install -y libmemcached-dev gcc libz-dev
RUN pip install -r ./requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]