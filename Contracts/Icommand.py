from abc import ABC, abstractmethod

class Icommand (ABC):
    @abstractmethod
    def Execute(self):
        pass
    @abstractmethod
    def Undo(self):
        pass