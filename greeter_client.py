import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        result = stub.Student(helloworld_pb2.StudentRequest(
            name="Ali",
            age=26
        ))
        return result


if __name__ == "__main__":
    response = run()
    print(response)
