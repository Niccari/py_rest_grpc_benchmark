#!/bin/bash

proto_name="api"
lib_path="./def_proto"

python3 -m grpc_tools.protoc $proto_name.proto --proto_path=. --python_out=$lib_path --grpc_python_out=$lib_path

# make (proto_name)_pb2_grpc importable.
sed -i '' -e "s/^import ${proto_name}_pb2/from . import ${proto_name}_pb2/" "$lib_path/${proto_name}_pb2_grpc.py"

python3 setup.py bdist_wheel
rm -r build *.egg-info
cp dist/*.whl ../client
cp dist/*.whl ../server
rm -r dist

echo "Success! libraries has been written in server/client directory."
