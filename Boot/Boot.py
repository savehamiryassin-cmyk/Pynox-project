from Kernel.kernel import MiniKernel  # type: ignore
from Kernel.filesystem import FileSystem # type: ignore

class BootManager:
    def __init__(self):
        self.kernel = MiniKernel()
        self.filesystem = FileSystem()
    def start(self):
        print("[BOOT] Starting Pynox...")
        print("[BOOT] Starting MiniKernel...")
        self.kernel.start()
        print("[BOOT] Initializing File System...")
        self.initializing_file_system()
        print("[BOOT] Pynox boot completed...")
    def initializing_file_system(self):
        directorys = [
            "system",
            "user",
            "applications",
            "temp"]
        for directory in directorys:
            self.filesystem.create_directory (directory)
        
        

