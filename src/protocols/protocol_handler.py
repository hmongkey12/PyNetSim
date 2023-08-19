from abc import ABC, abstractmethod

class ProtocolHandler(ABC):
    @abstractmethod
    def handle_update(self, router, message):
        pass  
