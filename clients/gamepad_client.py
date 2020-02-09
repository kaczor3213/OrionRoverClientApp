import inputs
import logging
import grpc
from generated_protos import gamepad_pb2, gamepad_pb2_grpc
from datetime import datetime
from time import sleep

def make_handshake(stub):
    response = stub.InitService(gamepad_pb2.msg_creq_StartConnection(content="Here OrionRover, do you copy?"))
    print("SERVER_RESP >>>\t",response)

def loop_ping(stub):
    while(True):
        ping_response = stub.TestConnection(gamepad_pb2.msg_Ping(content="Do you copy?"))
        print(f"CONN_STATUS ({str(datetime.now().time())}) >>>\t",ping_response.content)
        sleep(5)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gamepad_pb2_grpc.GamepadStub(channel)
        print("-------------- InitService --------------")
        make_handshake(stub)
        loop_ping(stub)
        

if __name__ == '__main__':
    logging.basicConfig()
    run()