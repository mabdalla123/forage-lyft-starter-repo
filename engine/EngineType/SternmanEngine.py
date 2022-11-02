from engine import engine
from abc import ABC, abstractmethod

class SternmanEngine(engine):
    @abstractmethod
    def needsService():
        pass
