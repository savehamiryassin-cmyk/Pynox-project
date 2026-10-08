import platform

def system():
    print("Pynox System Service")
    print("--------------------")
    print(f"OS:{platform.system()}")
    print(f"Architecture:{platform.machine()}")
    print(f"CPU:{platform.processor()}")
    print(f"python :{platform.python_version()}")