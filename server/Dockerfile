FROM python:3.9-slim

WORKDIR /app
COPY *.py /app/
COPY requirements.txt /app
COPY serve.sh /app

RUN python -m pip install -r requirements.txt

CMD ["./serve.sh"]
