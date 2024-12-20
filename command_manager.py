from typing import List


from factories.os_factory import OSFactory
from contracts.icommand import Icommand
from managers.abstract_managers.volume_manager import VolumeManager
from commands.increase_volume_command import IncreaseVolumeCommand
class CommandManager:
    def __init__(self, osFactory: OSFactory):
        self.osFactory = osFactory
        self.commands = []
        self.__add_default_commands()
        
    def add_command(self, command:Icommand):
        self.commands.append(command)
    def Execute_command(self, index):
         if 0 <= index < len(self.commands):
            cmd:Icommand = self.commands[index]
            cmd.Execute()
    def __add_default_commands(self):
        volume_manager:VolumeManager = self.osFactory.CreateVolumeManager()
        c = IncreaseVolumeCommand(volume_manager)
        self.add_command(c)
        
        
        
        