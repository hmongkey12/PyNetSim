from abc import ABC, abstractmethod
from typing import Any
class Router:
    pass

class ProtocolHandler(ABC):
    @abstractmethod
    def handle_update(self, router: Router, message: Any) -> None:
        pass
