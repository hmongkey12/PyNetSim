from protocols.protocol_handler import ProtocolHandler
from typing import Any, Dict, Tuple

class Router:
    def __init__(self, router_id: int) -> None:
        self.router_id: int = router_id
        self.neighbors: Dict[int, int] = {}
        self.routing_table: Dict[int, Tuple[None, int]] = {router_id: (None, 0)}

    def add_neighbor(self, neighbor_id: int, cost: int) -> None:
        self.neighbors[neighbor_id] = cost

    def update_routing_table(self, protocol_handler: ProtocolHandler, message: Any) -> None:
        protocol_handler.handle_update(self, message)

    def remove_neighbor(self, neighbor_id: int) -> None:
        if neighbor_id in self.neighbors:
            del self.neighbors[neighbor_id]

    def __str__(self) -> str:
        return f"Router {self.router_id}, Neighbors: {self.neighbors}, Routing Table: {self.routing_table}"
