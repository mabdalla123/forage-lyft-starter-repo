from engine import engine
from abc import ABC, abstractmethod

class CapuletEngine(engine):
    @abstractmethod
    def needsService():
        pass
