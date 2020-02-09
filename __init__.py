from services import gamepad_server
from clients import gamepad_client
from multiprocessing import Process, Queue
import logging

def run_client():
    gamepad_client.run()

def run_server():
    gamepad_server.serve()
    
if __name__ == "__main__":
    logging.basicConfig()
    q = Queue()
    
    server_process = Process(target=run_server)
    server_process.start()
    
    client_process = Process(target=run_client)
    client_process.start()
    
    print(q.get())