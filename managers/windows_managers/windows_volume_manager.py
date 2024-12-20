from ..abstract_managers.volume_manager import VolumeManager
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class WindowsVolumeManager(VolumeManager):
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        self.interface = devices.Activate(
            IAudioEndpointVolume._iid_, 1, None)
        self.volume = self.interface.QueryInterface(IAudioEndpointVolume)
    
    def GetCurrentVolume(self):
        return self.volume.GetMasterVolumeLevelScalar()
    
    def SetCurrentVolume(self, volume: float):
        if 0.0 <= volume <= 1.0:
            self.volume.SetMasterVolumeLevelScalar(volume, None)
    
    def MuteVolume(self):
        self.volume.SetMute(True, None)
    
    def IncreaseVolume(self):
        current_volume = self.GetCurrentVolume()
        new_volume = min(current_volume + 0.1, 1.0)   
        self.SetCurrentVolume(new_volume)
    
    def DecreaseVolume(self):
        # Decrease the volume by 10%
        current_volume = self.GetCurrentVolume()
        new_volume = max(current_volume - 0.1, 0.0)   
        self.SetCurrentVolume(new_volume)
