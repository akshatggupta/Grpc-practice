import grpc
import student_pb2
import student_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = student_pb2_grpc.StudentServiceStub(channel)

#Adding student
Response = stub.AddStudent(
    student_pb2.Student(
        name = "Akshat Gupta",
        class_name = "CSE",
        phone_no = "XXXXXXX114"
    )
)
print(Response.message)

#get all list of student
student = stub.GetStudent(student_pb2.empty())
for s in student.students:
    print(s.id, s.name , s.class_name , s.phone_no )

#edit student

Response = stub.EditStudent(
    student_pb2.Student(
        id =1,
        name = "Akshat GG",
        class_name = "CSE",
        phone_no = "XXXXXXX114"
        
    )
)
print(Response.message)

#delete student
Response = stub.DeleteStudent(student_pb2.StudentID(id=1))
print(Response.message)



