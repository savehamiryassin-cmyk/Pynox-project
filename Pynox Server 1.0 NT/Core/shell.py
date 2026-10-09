import os
import platform
import datetime
from service_manager import Service_manager
class PynoxShell:
    def __init__(self):
        self.name = "Pynox Shell"
        self.version = "1.0"
        self.status = "READY"
    def load(self):
        print("Pynox NT Shell Loaded")
        print(f"Shell Status:{self.status}")


    def Terminal(self):
        red_line = ["Windows", "System32", "Pynox","//","mnt","network"]
        if platform.system() == "Windows":
            if not os.path.isdir("C:\\Pynox"):
                os.mkdir("C:\\Pynox")
                os.chdir("C:\\Pynox")
            else:
                print("Pynox Folder Exists")
                os.chdir("C:\\Pynox")
            cd_input ="C:\\Pynox"
        while True:
            try:
                User1 = input(f"{os.getcwd()}>")
                User = User1.strip()
                manager = Service_manager()
                if User == "shutdown":
                    if platform.system() == "Windows":
                        os.system("shutdown /s /t 30")
                    print("System is shutting down...")
                elif User == "help":
                    print("Pynox Server 1.0 NT Shell")
                    print("shutdown for Quit and shut down ")
                    print("help for help")
                    print("Cancel for cancel shut down")
                    print("system info for system properties")
                    print("exit for quit Pynox")
                    print("dir for show files and directories")
                    print("cd folder to change directory")
                    print("date for current date")
                    print("time for current time")
                elif User == "cancel":
                    if platform.system() == "Windows":
                        os.system("shutdown /a")
                    print("System is cancel shutting down...")
                elif User.startswith("dir "):
                    dir_input = User[3:]
                    os.system("dir "+dir_input)
                elif User == "dir":
                    os.system("dir")
                elif User.startswith("cd "):
                    cd_input = User[3:].strip()
                    if cd_input == ".":
                        os.chdir(cd_input)
                    elif cd_input == "..":
                        cd_input = os.path.dirname(os.getcwd())
                        os.chdir(cd_input)
                        print(f"change directory to {cd_input} Completed")
                    elif cd_input == " " or cd_input == "":
                        os.chdir(cd_input)
                    else:
                        if os.path.isdir(cd_input):
                            os.chdir(cd_input)
                            os.system("dir")
                            print(f"change directory to {os.getcwd()} Completed")
                        else:
                            print("Folder not found")
                elif User.startswith("mkdir "):
                    mkdir_input = User[6:].strip()
                    if os.path.isdir(mkdir_input):
                        print("this folder already exists")
                    elif mkdir_input == "" or mkdir_input == " ":
                        print("Try again")
                    else:
                        os.mkdir(mkdir_input)
                        os.system("dir")
                        print("Make directory Completed")
                elif User.startswith("rmdir "):
                    rmdir_input = User[6:].strip()
                    if not os.path.isdir(rmdir_input):
                        print("this directory not found")
                    elif rmdir_input == "" or rmdir_input == " ":
                        print("Try again")
                    elif rmdir_input not in red_line:
                        os.rmdir(rmdir_input)
                        os.system("dir")
                        print("Remove directory Completed")
                elif User.startswith("delete "):
                    del_input = User[6:].strip()
                    if del_input == "" or del_input == " ":
                        print("Try again")
                    elif del_input not in red_line:
                        os.remove(del_input)
                        os.system("dir")
                elif User == "pynox network service start":
                    manager.network()
                elif User == "pynox storage service start":
                    manager.storage()
                elif User == "pynox process service start":
                    manager.process()
                elif User == "pynox system service start":
                    manager.system()
                elif User == "pynox time service start":
                    manager.time()
                elif User.startswith("pynox program service run "):
                    manager.program(User)
                elif User == "list services":
                    manager.list_service()
                elif User == "exit":
                    break
            except FileNotFoundError:
                print("External ERROR: File or Dirctory not found")
            except PermissionError:
                print("External ERROR: Access denied")
            except NotADirectoryError:
                print("External ERROR: Directory not found")
            except OSError as e:
                print(f"External ERROR {e}")
            