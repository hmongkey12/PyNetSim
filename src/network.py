from typing import Dict, List, Tuple
from router import Router
from protocols.protocol_handler import ProtocolHandler

class Network:
    def __init__(self) -> None:
        self.routers: Dict[int, Router] = {}
        self.links: List[Tuple[Router, Router, int]] = []

    def add_router(self, router_id: int) -> Router:
        router = Router(router_id)
        self.routers[router_id] = router
        return router

    def create_link(self, router1: Router, router2: Router, cost: int) -> None:
        router1.add_neighbor(router2.router_id, cost)
        router2.add_neighbor(router1.router_id, cost)
        self.links.append((router1, router2, cost))

    def simulate(self, protocol_handler: ProtocolHandler, iterations: int = 10) -> None:
        for _ in range(iterations):
            for router in self.routers.values():
                router.update_routing_table(protocol_handler, None) # Message depends on protocol
