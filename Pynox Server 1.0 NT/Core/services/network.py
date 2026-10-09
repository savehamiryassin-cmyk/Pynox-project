import socket as net
import platform
def network_status():
    host = net.gethostname()
    DNS = net.gethostbyname("example.com")
    print("Pynox Network Service")
    print("---------------------")
    print(f"Hostname:{host}")
    print(f"IP:{net.gethostbyname(host)}")
    print(f"DNS:{DNS}")
    try:
        print(f"System:{platform.system()}")
    except socket.gaierror:
        print("DNS found error")

