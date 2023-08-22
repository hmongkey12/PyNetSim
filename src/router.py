from typing import Any, Dict
from protocols.protocol_handler import ProtocolHandler
from dataclasses import dataclass


@dataclass
class RoutingEntry:
    next_hop: int
    cost: int


class Router:
    def __init__(self, router_id: int) -> None:
        self.router_id: int = router_id
        self.neighbors: Dict[int, int] = {}
        self.routing_table: Dict[int, RoutingEntry] = {
            # Using the dataclass RoutingEntry
            router_id: RoutingEntry(next_hop=None, cost=0)
        }

    def add_neighbor(self, neighbor_id: int, cost: int) -> None:
        self.neighbors[neighbor_id] = cost
        self.routing_table[neighbor_id] = RoutingEntry(
            next_hop=neighbor_id, cost=cost)  # Using the dataclass RoutingEntry

    def update_routing_table(self, protocol_handler: ProtocolHandler, message: Any) -> None:
        protocol_handler.handle_update(
            self.routing_table, self.neighbors, message)

    def remove_neighbor(self, neighbor_id: int) -> None:
        if neighbor_id in self.neighbors:
            del self.neighbors[neighbor_id]
            del self.routing_table[neighbor_id]

    def __str__(self) -> str:
        return f"Router {self.router_id}, Neighbors: {self.neighbors}, Routing Table: {self.routing_table}"
