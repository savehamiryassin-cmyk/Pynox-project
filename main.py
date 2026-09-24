import os
import shell
from kernel import Pynox_NT_Kernel
from file_system import PynoxFileSystem

kernel = Pynox_NT_Kernel()
file_system = PynoxFileSystem()
shell = shell.PynoxShell()


boot_status = True
files = ["main.py","kernel.py","shell.py","file_system.py"]
print("Pynox Server 1.0")
print("\n""Checking system files...")
for file in files:
    if not os.path.isfile(file):
        print(f"{file} not found")
        boot_status = False
    else:
        print(f"{file} [OK]")

if boot_status:
    print("\n""System file verified...")
    print("Loading Pynox NT Kernel...")
    kernel.load()
    print("Loading Pynox File System...")
    file_system.load()
    print("Loading Pynox Shell...")
    shell.load()
Terminal = shell.Terminal()
