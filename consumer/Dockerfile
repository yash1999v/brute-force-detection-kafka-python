FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY consumer.py .

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh


CMD ["python", "consumer.py"]
