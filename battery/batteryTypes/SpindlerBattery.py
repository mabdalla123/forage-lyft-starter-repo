from battery import battery
from abc import ABC, abstractmethod

class SpindlerBattery(battery):
    @abstractmethod
    def needsService():
        pass
