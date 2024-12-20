
import platform

from command_manager import CommandManager
from factories.windows_factory import WindowsFactory
def main():
    Factory = MakeFactory()
    c = CommandManager(Factory)
    c.Execute_command(0) #Increases volume by 10%
    
def MakeFactory():
    current_os = platform.system()  
    if current_os == "Windows":
        print("The OS is Windows.")
        return WindowsFactory()
    elif current_os == "Linux":
        print("The OS is Linux.")
        #TODO : Make Linux factory
    elif current_os == "Darwin":  
        print("The OS is macOS.")
        #TODO : Make MacOS factory
    else:
        print("Unknown OS.")

if __name__ == "__main__":
    main()
