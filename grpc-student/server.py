import grpc
from concurrent import futures
import student_pb2
import student_pb2_grpc


class StudentService(student_pb2_grpc.StudentServiceServicer):

    def __init__(self):
        self.students = {}
        self.counter = 1

    def AddStudent(self, request, context):
        request.id = self.counter
        self.students[self.counter] = request
        self.counter += 1
        return student_pb2.Response(message="Student added successfully")

    def GetStudent(self, request, context):
        return student_pb2.StudentList(students=self.students.values())

    def DeleteStudent(self, request, context):
        if request.id not in self.students:
            return student_pb2.Response(message="Student not found")

        del self.students[request.id]
        return student_pb2.Response(message="Student deleted successfully")

    def EditStudent(self, request, context):
        if request.id not in self.students:
            return student_pb2.Response(message="Student not found")

        self.students[request.id] = request
        return student_pb2.Response(message="Student edited successfully")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    student_pb2_grpc.add_StudentServiceServicer_to_server(
        StudentService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print(" gRPC Server running on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
