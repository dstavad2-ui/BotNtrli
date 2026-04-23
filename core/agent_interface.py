from abc import ABC, abstractmethod

class NaturligAgent(ABC):
    @abstractmethod
    def execute(self, task, context=None):
        pass

    @abstractmethod
    def register(self, registry):
        pass
