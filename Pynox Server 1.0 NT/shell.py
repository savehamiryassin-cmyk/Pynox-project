import os
import platform
import datetime
class PynoxShell:
    def __init__(self):
        self.name = "Pynox Shell"
        self.version = "1.0"
        self.status = "READY"
    def load(self):
        print("Pynox NT Shell Loaded")
        print(f"Shell Status:{self.status}")


    def Terminal(self):
        red_line = ["Windows", "System32", "Pynox"]
        if not os.path.isdir("C:\\Pynox"):
            os.mkdir("C:\\Pynox")
            os.chdir("C:\\Pynox")
        else:
            print("Pynox Folder Exists")
            os.chdir("C:\\Pynox")
            red_line = ["Windows", "System32", "Pynox"]
        cd_input ="C:\\Pynox"
        while True:
            User1 = input(f"{cd_input}>")
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
                print("dir for show files and directories")
                print("cd folder to change directory")
                print("date for current date")
                print("time for current time")
            elif User == "cancel":
                os.system("shutdown /a")
                print("System is cancel shutting down...")
            elif User == "dir":
                dir_input = input("enter folder path:")
                os.system("dir "+dir_input)
            elif User == "cd":
                cd_input = input("enter folder path:")
                if cd_input == "." or cd_input == "..":
                    cd_input = "C:\\Pynox"
                    os.system("cd " + cd_input)
                    print(f"change directory to {cd_input} Completed")
                elif cd_input == " " or cd_input == "":
                    cd_input = "C:\\Pynox"
                    os.system("cd " + cd_input)
                else:
                    if os.path.isdir(cd_input):
                        os.system("cd " + cd_input)
                        os.system("dir " + cd_input)
                        print(f"change directory to {cd_input} Completed")
                    else:
                        print("Folder not found")
                        cd_input = "C:\\Pynox"
            elif User == "mkdir":
                mkdir_input = input("enter folder name :")
                if os.path.isdir(mkdir_input):
                    print("this folder already exists")
                elif mkdir_input == "" or mkdir_input == " ":
                    print("Try again")
                else:
                    os.system("mkdir " + mkdir_input)
                    os.system("dir")
                    print("Make directory Completed")
            elif User == "rmdir":
                rmdir_input = input("enter folder name :")
                if not os.path.isdir(rmdir_input):
                    print("this directory not found")
                elif rmdir_input == "" or rmdir_input == " ":
                    print("Try again")
                elif rmdir_input not in red_line:
                    os.system("rmdir " + rmdir_input)
                    os.system("dir")
                    print("Remove directory Completed")
            elif User == "delete":
                del_input = input("enter file  name :")
                red_line = ["Windows","System32","Pynox"]
                if del_input == "" or del_input == " ":
                    print("Try again")
                elif del_input not in red_line:
                    os.system("del " + del_input)
                    os.system("dir")



            elif User == "date":
                print(datetime.date.today())
            elif User == "time":
                now = datetime.datetime.now()
                print(f"{now.hour}:{now.minute}:{now.second}")

            elif User == "system info":
                print(f"Platform:{platform.system()}")
                print(f"Architecture:{platform.machine()}")
                print(f"python version:{platform.python_version()}")
                print(f"kernel version of {platform.system()}:{platform.version()}")
            elif User == "exit":
                break











