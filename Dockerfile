FROM python:3.9.5-slim

COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-w 8", "-b 0.0.0.0:8000", "-k uvicorn.workers.UvicornWorker", "main:app"]