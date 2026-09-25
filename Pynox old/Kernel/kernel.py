class MiniKernel:
    def __init__(self):
        self.name = "Pynox Mini"
        self.status = "Stoped"
        self.version = "1.0"
    def start(self):
        self.status = "Runnig"
        print(f"{self.name} Started.")
    def Stop(self):
        self.status = "Stoped"
        print(f"{self.name} stoped")
    def info(self):
        print(f"Kernel:{self.name}")
        print(f"Version:{self.version}")
        print(f"Status:{self.status}")
