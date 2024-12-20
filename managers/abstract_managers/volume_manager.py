from abc import ABC, abstractmethod

class VolumeManager (ABC):
    @abstractmethod
    def GetCurrentVolume(self):
        pass
    @abstractmethod
    def SetCurrentVolume(self):
        pass
    @abstractmethod
    def MuteVolume(self):
        pass
    @abstractmethod
    def IncreaseVolume(self):
        pass
    @abstractmethod
    def DecreaseVolume(self):
        pass