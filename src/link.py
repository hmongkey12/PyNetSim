class Link:
    def __init__(self, router1, router2, cost):
        self.router1 = router1
        self.router2 = router2
        self.cost = cost

    def connect_routers(self):
        self.router1.add_neighbor(self.router2.router_id, self.cost)
        self.router2.add_neighbor(self.router1.router_id, self.cost)

    def disconnect_routers(self):
        self.router1.remove_neighbor(self.router2.router_id)
        self.router2.remove_neighbor(self.router1.router_id)
