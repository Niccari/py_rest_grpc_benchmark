#!/bin/bash

uvicorn rest_server:app --host 0.0.0.0 --port 8000 --workers 2 &
python3 grpc_server.py &

while true;
do
    sleep 10000
done
