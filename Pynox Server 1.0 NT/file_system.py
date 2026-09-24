class PynoxFileSystem:
    def __init__(self):
        self.name = "Pynox File System"
        self.version = "1.0"
        self.status = "READY"
    def load(self):
        print("Pynox File System Loaded")
        print(f"File system status:{self.status}")
