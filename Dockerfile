FROM python:3.9.5-slim

COPY . .
RUN pip install -r ./requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]