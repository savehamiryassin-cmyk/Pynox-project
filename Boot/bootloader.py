
class Bootloader:
    def __init__(self):
        self.status = "Ready"
    def load(self):
        print("[BOOTLOADER] Loading Pynox...")
        self.status = "Loaded"
        print("[BOOTLOADER] Bootloader finished.")
