from typing import Dict
from router import Router
from protocols.protocol_handler import ProtocolHandler
from factories.router_factory import RouterFactory
from managers.link_manager import LinkManager


class Network:
    def __init__(self, router_factory: RouterFactory, link_manager: LinkManager) -> None:
        self.routers: Dict[int, Router] = {}
        self.router_factory = router_factory
        self.link_manager = link_manager

    def add_router(self, router_id: int) -> Router:
        router = self.router_factory.create_router(router_id)
        self.routers[router_id] = router
        return router

    def create_link(self, router1: Router, router2: Router, cost: int) -> None:
        self.link_manager.create_link(router1, router2, cost)

    def simulate(self, protocol_handler: ProtocolHandler, iterations: int = 10) -> None:
        for _ in range(iterations):
            for router in self.routers.values():
                # Message depends on protocol
                router.update_routing_table(protocol_handler, None)
