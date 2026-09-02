
from pathlib import Path

class FileSystem:
    def __init__(self):
        self.root = Path("PynoxData")
        self.root.mkdir(exist_ok = True)
    def create_directory(self,name):
        directory = self.root / name
        directory.mkdir(exist_ok=True)    
    def list_directory(self):
        return list(self.root.iterdir())

