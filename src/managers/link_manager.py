from link import Link


class LinkManager:
    def __init__(self):
        self.links = []

    def create_link(self, router1, router2, cost):
        link = Link(router1, router2, cost)
        link.connect_routers()
        self.links.append(link)
