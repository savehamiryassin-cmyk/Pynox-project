import shutil

def status():
    total, used , free = shutil.disk_usage("C:\\")
    print("Pynox storage service")
    print("---------------------")
    print(f"Total: {total // (1024 ** 3)}GB")
    print(f"Used: {used // (1024 ** 3)}GB")
    print(f"Free: {free // (1024 ** 3)}GB")
