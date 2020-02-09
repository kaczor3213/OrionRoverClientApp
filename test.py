from generated_protos import gamepad_pb2_grpc
import grpc

channel = grpc.insecure_channel('localhost:50051')
stub = gamepad_pb2_grpc.GamepadEventsStub(channel)
