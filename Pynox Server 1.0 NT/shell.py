import os
import platform
class PynoxShell:
    def __init__(self):
        self.name = "Pynox Shell"
        self.version = "1.0"
        self.status = "READY"
    def load(self):
        print("Pynox NT Shell Loaded")
        print(f"Shell Status:{self.status}")


    def Terminal(self):
        while True:
            User1 = input("C:\\Pynox> ")
            User_stp = User1.strip()
            User = User_stp.lower()
            if User == "shutdown":
                os.system("shutdown /s /t 60")
                print("System is shutting down...")
            elif User == "help":
                print("Pynox Server 1.0 NT Shell")
                print("shutdown for Quit and shut down ")
                print("help for help")
                print("Cancel for cancel shut down")
                print("system info for system properties")
                print("exit for quit Pynox")
            elif User == "cancel":
                os.system("shutdown /a")
                print("System is cancel shutting down...")
            elif User == "dir":
                dir_input = input("enter folder path:")
                os.system("dir "+dir_input)
            elif User == "system info":
                print(f"Platform:{platform.system()}")
                print(f"Architecture:{platform.machine()}")
                print(f"python version:{platform.python_version()}")
                print(f"kernel version of {platform.system()}:{platform.version()}")
            elif User == "exit":
                break
            elif User == "dir":
                dir_input = input("enter folder path:")
                os.system("dir "+dir_input)










