from contracts.icommand import Icommand
from managers.abstract_managers.volume_manager import VolumeManager

class IncreaseVolumeCommand(Icommand):
    def __init__(self, VolumeManager: VolumeManager) -> None:
        super().__init__() 
        self.VolumeManager:VolumeManager = VolumeManager
        
    def Execute(self):
        self.VolumeManager.IncreaseVolume()
    def Undo(self):
        pass