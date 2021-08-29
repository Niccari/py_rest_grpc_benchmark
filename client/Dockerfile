FROM python:3.9-slim

WORKDIR /app
COPY *.py /app
COPY requirements.txt /app
COPY mock_data /app/mock_data

RUN python -m pip install -r requirements.txt

CMD ["python3", "main.py"]

