from concurrent import futures

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def Student(self, request, context):
        students = [
            {"name": "Ali", "age": 26, "course": 3},
            {"name": "Dali", "age": 23, "course": 1},
        ]

        course = 0
        for student in students:
            if student["name"] == request.name:
                course = student["course"]

        response = helloworld_pb2.StudentReply(
            course=course
        )
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Server started...")
    serve()
