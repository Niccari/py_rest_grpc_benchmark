#!/bin/bash

proto_name="api"

python3 -m grpc_tools.protoc $proto_name.proto --proto_path=. --python_out=. --grpc_python_out=.

cp $proto_name*pb2*.py ../client
cp $proto_name*pb2*.py ../server

rm *pb2*.py
