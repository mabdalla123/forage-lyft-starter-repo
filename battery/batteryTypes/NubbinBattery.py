from battery import battery
from abc import ABC, abstractmethod

class NubbinBattery(battery):
    @abstractmethod
    def needsService():
        pass
