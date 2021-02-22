from __future__ import print_function
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name = 'you'))
        print(response.message)
        response = stub.SayHelloAgin(helloworld_pb2.HelloRequest(name = 'you'))
        print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()