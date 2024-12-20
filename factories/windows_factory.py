from factories.os_factory import OSFactory
from managers.windows_managers.windows_volume_manager import WindowsVolumeManager
class WindowsFactory (OSFactory):
    def CreateVolumeManager(self):
        return WindowsVolumeManager()
    def CreateBrightnessManager(self):
        pass