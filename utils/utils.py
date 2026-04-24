import socket
import time

def resolve_host(host):
    try:
        return socket.gethostbyname(host)
    except:
        return "Resolution Failed"


def measure_latency(host, port):
    try:
        start = time.time()

        sock = socket.socket()
        sock.settimeout(3)
        sock.connect((host, port))

        end = time.time()
        sock.close()

        return round((end - start) * 1000, 2)

    except:
        return "Timeout"