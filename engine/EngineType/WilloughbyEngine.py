from engine import engine
from abc import ABC, abstractmethod

class WilloughbyEngine(engine):
    @abstractmethod
    def needsService():
        pass
