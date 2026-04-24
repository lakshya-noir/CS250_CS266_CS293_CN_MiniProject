import socket
import ssl

def grab_banner(host, port):
    try:
        sock = socket.socket()
        sock.settimeout(3)

        if port == 443:
            context = ssl.create_default_context()
            sock = context.wrap_socket(sock, server_hostname=host)
        sock.connect((host, port))

        request = (
            f"HEAD / HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            f"User-Agent: FingerprintTool\r\n"
            f"Connection: close\r\n\r\n"
        )

        sock.send(request.encode())
        response = sock.recv(4096).decode(errors="ignore")
        sock.close()

        headers = response.split("\r\n")o
        return "\n".join(headers)

    except Exception as e:
        return f"Error grabbing banner: {e}"