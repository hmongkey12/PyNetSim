from abc import ABC, abstractmethod
from typing import Any, Dict
from collections import namedtuple


class Router:  # Forward declaration
    pass


RoutingEntry = namedtuple('RoutingEntry', ['next_hop', 'cost'])


class ProtocolHandler(ABC):
    @abstractmethod
    def handle_update(self, routing_table: Dict[int, RoutingEntry], neighbors: Dict[int, int], message: Any) -> None:
        pass
