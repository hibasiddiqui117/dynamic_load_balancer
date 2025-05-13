# server.py

class Server:
    def __init__(self, id, max_capacity):
        self.id = id
        self.max_capacity = max_capacity
        self.current_load = 0

    def can_accept(self, request_load):
        return self.current_load + request_load <= self.max_capacity

    def assign_request(self, request_load):
        if self.can_accept(request_load):
            self.current_load += request_load
            return True
        return False

    def release_load(self, load):
        self.current_load = max(0, self.current_load - load)

    def __repr__(self):
        return f"Server-{self.id}: Load={self.current_load}/{self.max_capacity}"
