from generated_protos import gamepad_pb2, gamepad_pb2_grpc
import grpc
from concurrent import futures
import logging
from datetime import datetime
class GamepadServicer(gamepad_pb2_grpc.GamepadServicer):
    def __init__(self):
        print("Gamepad service initialized!")
        
    def InitService(self, request, context):
        if request is None:
            return gamepad_pb2.msg_sres_StartConnection(content="Connection failed :(\n")
        else:
            return gamepad_pb2.msg_sres_StartConnection(content="Copy, here OrionRover!\n")

    def TestConnection(self, request, context):
        if request is None:
            print("No client connected! :(")
            return None
        else:
            return gamepad_pb2.msg_Ping(content=f"Copy, here OrionRover! ({str(datetime.now().time())})\n")
    
    def ButtonEvent(self, request, context):
        if request is None:
            return gamepad_pb2.msg_sres_ButtonEventTransfer(btn_name="Failed to obtain button name :(\n")
        else:
            return gamepad_pb2.msg_sres_ButtonEventTransfer(btn_name=f"Received btn name: {request.btn_name}\n")
        
    def TransmitLS(self, request_iterator, context):
        for ls in request_iterator:
            print(ls.x_offset,ls.y_offset)
            yield ls
            
    def TransmitRS(self, request_iterator, context):
        for rs in request_iterator:
            print(rs.x_offset,rs.y_offset)
            yield rs
            
    def TransmitLT(self, request_iterator, context):
        for lt in request_iterator:
            print(lt.z_offset)
            yield lt
            
    def TransmitRT(self, request_iterator, context):
        for rt in request_iterator:
            print(rt.z_offset)
            yield rt
            
def serve():
    print("Server start")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gamepad_pb2_grpc.add_GamepadServicer_to_server(
        GamepadServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()