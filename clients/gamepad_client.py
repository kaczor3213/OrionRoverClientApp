from __future__ import print_function

import inputs
import logging
import grpc
from ..generated_protos import gamepad_pb2, gamepad_pb2_grpc

def guide_get_one_feature(stub, point):
    feature = stub.GetFeature(point)
    if not feature.location:
        print("Server returned incomplete feature")
        return

    if feature.name:
        print("Feature called %s at %s" % (feature.name, feature.location))
    else:
        print("Found no feature at %s" % feature.location)

def make_handshake(stub):
    gamepad_pb2.CallRover(hello_message="Her OrionRover, do you copy?")
    
    
    guide_get_one_feature(stub, route_guide_pb2.Point(latitude=0, longitude=0))



def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gamepad_pb2_grpc.GamepadEventsStub(channel)
        print("-------------- GetFeature --------------")
        guide_get_feature(stub)
        print("-------------- ListFeatures --------------")
        guide_list_features(stub)
        print("-------------- RecordRoute --------------")
        guide_record_route(stub)
        print("-------------- RouteChat --------------")
        guide_route_chat(stub)

if __name__ == '__main__':
    logging.basicConfig()
    run()