from protocols.protocol_handler import ProtocolHandler
from collections import namedtuple, defaultdict
from typing import Any, Dict

RoutingEntry = namedtuple('RoutingEntry', ['next_hop', 'cost'])


class RipProtocol(ProtocolHandler):
    def handle_update(self, routing_table: Dict[int, RoutingEntry], neighbors: Dict[int, int], message: Any) -> None:
        # Initialize new_routing_table with the existing routing table entries
        new_routing_table = routing_table.copy()

        # Iterate through neighbors and apply RIP logic
        for neighbor, cost in neighbors.items():
            # Assume the neighbor's routing table is passed in the message
            neighbor_routing_table = message.get(neighbor)
            if neighbor_routing_table:
                for dest, entry in neighbor_routing_table.items():
                    # If a better path is found through a neighbor, update the routing entry
                    if dest not in new_routing_table or entry.cost + cost < new_routing_table[dest].cost:
                        new_routing_table[dest] = RoutingEntry(
                            next_hop=neighbor, cost=entry.cost + cost)

        # Update the original routing table with the newly calculated values
        routing_table.clear()
        routing_table.update(new_routing_table)
