from abc import ABC, abstractmethod

class OSFactory (ABC):
    @abstractmethod
    def CreateVolumeManager(self):
        pass
    @abstractmethod
    def CreateBrightnessManager(self):
        pass