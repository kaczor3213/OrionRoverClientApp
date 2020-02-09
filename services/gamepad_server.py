from generated_protos import gamepad_pb2, gamepad_pb2_grpc
import grpc
from concurrent import futures
import logging

class GamepadEventsServicer(gamepad_pb2_grpc.GamepadEventsServicer):
    def InitService(self, request, context):
        received_message=request
        if received_message is None:
            return gamepad_pb2.RoverFeedback(hello_response="Connection failed :(\n")
        else:
            return gamepad_pb2.RoverFeedback(hello_response="Copy, here OrionRover!\n")

    def ButtonEvent(self, request, context):
        button_name=request
        if button_name is None:
            return gamepad_pb2.RoverFeedback(btn_name="Failed to obtain button name :(\n")
        else:
            return gamepad_pb2.RoverFeedback(btn_name=f"Received btn name: {button_name}\n")
        
        
    def TransmitLS(self, request_iterator, context):
        for ls in request_iterator:
            print(ls)
            yield ls
            
    def TransmitRS(self, request_iterator, context):
        for rs in request_iterator:
            print(rs)
            yield rs
            
    def TransmitLT(self, request_iterator, context):
        for lt in request_iterator:
            print(lt)
            yield lt
            
    def TransmitRT(self, request_iterator, context):
        for rt in request_iterator:
            print(rt)
            yield rt
            
def serve():
    print("Server start")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gamepad_pb2_grpc.add_GamepadEventsServicer_to_server(
        GamepadEventsServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()