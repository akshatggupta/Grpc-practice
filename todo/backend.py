import grpc
from concurrent import futures
import todo_pb2_grpc
import todo_pb2

class TodoService(todo_pb2_grpc.TodoServiceServicer):

    def __init__(self):
        self.todos = {}
        self.counter = 1

    def AddTodo(self, request, context):
        request.id = self.counter
        self.todos[self.counter] = request
        self.counter +=1
        return todo_pb2.Response(message = "Todo added succesfully")

    def ViewTodo(self, request, context):
        return todo_pb2.TodoList(todos = self.todos.values())

    def DeleteTodo(self, request, context):
        if request.id not in self.todos:
            return todo_pb2.Response(message = "Todo not found")
        del self.todos[request.id]
        return todo_pb2.Response(message = "Item Deleted succesfully")
        
    def EditTodo(self, request, context):
        if request.id not in self.todos:
            return todo_pb2.Response(message = "Todo not found")
        self.todos[request.id] = request
        return todo_pb2.Response(message = "Todo Edited Succesfully")

def serves():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServiceServicer_to_server(
        TodoService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print(" gRPC Server running on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serves()
