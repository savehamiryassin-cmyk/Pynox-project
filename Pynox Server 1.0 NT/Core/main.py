import os
import shell
from kernel import Pynox_NT_Kernel


kernel = Pynox_NT_Kernel()
shell = shell.PynoxShell()


boot_status = True
files = ["main.py","kernel.py","shell.py","service_manager.py"]
print("Pynox Server 1.0")
print("----------------")
print("Checking system files...")
for file in files:
    if not os.path.isfile(file):
        pass
    else:
        print(f"{file} [OK]")

Terminal = shell.Terminal()
