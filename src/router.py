from protocols.protocol_handler import ProtocolHandler

class Router:
    def __init__(self, router_id: int):
        self.router_id = router_id
        self.neighbors = {}
        self.routing_table = {router_id: (None, 0)}

    def add_neighbor(self, neighbor_id: int, cost: int):
        self.neighbors[neighbor_id] = cost

    def update_routing_table(self, protocol_handler: ProtocolHandler, message):
        protocol_handler.handle_update(self, message)

    def __str__(self):
        return f"Router {self.router_id}, Neighbors: {self.neighbors}, Routing Table: {self.routing_table}"

