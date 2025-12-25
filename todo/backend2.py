import grpc
import todo_pb2
import todo_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = todo_pb2_grpc.TodoServiceStub(channel)


# Adding Todo
while True:
    print("\n1. Add Todo")
    print("2. View Todo")
    print("3. Delete Todo")
    print("4. Edit Todo")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter todo: ")
        response = stub.AddTodo(
            todo_pb2.Todo(
                name=name
            )
        )
        print(response.message)

    elif choice == "2":
        # get all list of Todo
        todo = stub.ViewTodo(todo_pb2.Empty())
        for s in todo.todos:
            print(s.id, s.name)

    elif choice == "3":
        # delete student
        a = int(input("enter the id of todo"))
        response = stub.DeleteTodo(todo_pb2.TodoId(id=a))
        print(response.message)

    elif choice == "4":
        response = stub.EditTodo(
            todo_pb2.Todo(
                id=1,
                name="Akshat GG"
            )
        )
        print(response.message)

    elif choice == "5":
        print("Exiting...")
        break