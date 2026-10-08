import socket as net
import platform
def network_status():
    host = net.gethostname()
    print("Pynox Network Service")
    print("---------------------")
    print(f"Hostname:{host}")
    print(f"IP:{net.gethostbyname(host)}")
    print(f"System:{platform.system()}")

