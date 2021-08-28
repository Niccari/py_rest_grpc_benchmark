from setuptools import setup

setup(
    name='def_proto',
    version='0.0.1',
    description='gRPC API protobuf definition',
    author='niccari',
    url='https://niccari.net/',
    install_requires=["grpcio", "protobuf"],
    packages=["def_proto"],
)
