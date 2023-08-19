from router import Router

class Network:
    def __init__(self):
        self.routers = {}
        self.links = []

    def add_router(self, router_id: int):
        router = Router(router_id)
        self.routers[router_id] = router
        return router

    def create_link(self, router1: Router, router2: Router, cost: int):
        router1.add_neighbor(router2.router_id, cost)
        router2.add_neighbor(router1.router_id, cost)
        self.links.append((router1, router2, cost))

    def simulate(self, protocol_handler, iterations=10):
        for _ in range(iterations):
            for router in self.routers.values():
                router.update_routing_table(protocol_handler, None) # Message depends on protocol

