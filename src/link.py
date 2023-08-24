from typing import List
from router import Router


class Link:
    def __init__(self, router1: Router, router2: Router, cost: int) -> None:
        self.router1: Router = router1
        self.router2: Router = router2
        self.cost: int = cost

    def connect_routers(self) -> None:
        self.router1.add_neighbor(self.router2.router_id, self.cost)
        self.router2.add_neighbor(self.router1.router_id, self.cost)

    def disconnect_routers(self) -> None:
        self.router1.remove_neighbor(self.router2.router_id)
        self.router2.remove_neighbor(self.router1.router_id)
