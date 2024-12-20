# from Commands.IncreaseVolumeCommand import *

# x = IncreaseVolumeCommand()

# x.Execute()

# x.Undo()



from managers.windows_managers.windows_volume_manager import WindowsVolumeManager



def main():
    # Create an instance of WindowsVolumeManager
    z = WindowsVolumeManager()
    print("WindowsVolumeManager object created:", z)

if __name__ == "__main__":
    main()
