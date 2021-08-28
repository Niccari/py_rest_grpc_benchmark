# py_rest_grpc_benchmark(gRPC and REST transaction benchmark by Python)

Measure the time which takes to send and receive data in REST and gRPC.

To assume microservices, two Docker containers will be used to configure the server and client.

```
gRPC: [Client container] <---> (host: server, port 22312) [Server container]
REST: [Client container] <---> (host: server, port 8000)  [Server container]

The server has two processes(gRPC server, uvicorn).
```

## Measurement pattern
## Rx
1. request=None、response={}
2. request={ "count": 1 }、response={ "data": [{"id": (random_10digit_int), "hoge": (random_16digit_alphanumeric) }] }
3. Set the "count" to 10.
4. Set the "count" to 50.
5. Set the "count" to 100.

gRPC uses unary RPC.

## Tx
1. Upload 1MB text file
2. Upload 5MB text file
3. Upload 30MB text file
4. Upload 1MB image file
5. Upload 5MB image file
6. Upload 30MB image file

gRPC uses client streaming RPC.

## Usage
Invoke `./run.sh` or `docker compose up` manually.

## Measurement Results
See `result_sample/`.

## Author
niccari
