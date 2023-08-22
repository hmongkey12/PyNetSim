from protocols.protocol_handler import ProtocolHandler
from typing import Any, Dict
from dataclasses import dataclass


@dataclass
class RoutingEntry:
    next_hop: int
    cost: int


class RipProtocol(ProtocolHandler):
    def handle_update(self, routing_table: Dict[int, RoutingEntry], neighbors: Dict[int, int], message: Any) -> None:
        # Copy existing routing table entries to a new one
        new_routing_table = routing_table.copy()

        # Iterate through neighbors and apply RIP logic
        for neighbor, cost_to_neighbor in neighbors.items():
            # Get the neighbor's routing table from the message
            neighbor_routing_table = message.get(neighbor)
            if neighbor_routing_table:
                # Update the new_routing_table based on the neighbor's routing table
                new_routing_table.update({
                    dest: RoutingEntry(next_hop=neighbor,
                                       cost=entry.cost + cost_to_neighbor)
                    for dest, entry in neighbor_routing_table.items()
                    if dest not in new_routing_table or entry.cost + cost_to_neighbor < new_routing_table[dest].cost
                })

        # Replace the original routing table with the newly calculated values
        routing_table.clear()
        routing_table.update(new_routing_table)
