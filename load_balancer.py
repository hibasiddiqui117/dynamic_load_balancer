# load_balancer.py

from server import Server
from config import NUM_SERVERS, MAX_SERVER_CAPACITY
import random

class LoadBalancer:
    def __init__(self):
        self.servers = [Server(i, MAX_SERVER_CAPACITY) for i in range(NUM_SERVERS)]

    def get_least_loaded_server(self):
        return min(self.servers, key=lambda s: s.current_load)

    def assign_request(self, request_load):
        server = self.get_least_loaded_server()
        if server.assign_request(request_load):
            print(f"Request with load {request_load} assigned to Server-{server.id}")
            return True
        else:
            print("All servers are overloaded!")
            return False

    def release_random_loads(self):
        for server in self.servers:
            if server.current_load > 0:
                load_to_release = random.randint(5, 15)
                server.release_load(load_to_release)
