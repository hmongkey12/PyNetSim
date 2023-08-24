from typing import List
from router import Router
from link import Link


class LinkManager:
    def __init__(self) -> None:
        self.links: List[Link] = []

    def create_link(self, router1: Router, router2: Router, cost: int) -> None:
        link: Link = Link(router1, router2, cost)
        link.connect_routers()
        self.links.append(link)
