import ssl
import socket

def get_ssl_info(host, port):
    info = {}

    try:
        context = ssl.create_default_context()

        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                info["TLS Version"] = ssock.version()
                info["Cipher"] = ssock.cipher()[0]
                info["Certificate Subject"] = dict(x[0] for x in ssock.getpeercert()["subject"])
                info["Issuer"] = dict(x[0] for x in ssock.getpeercert()["issuer"])

    except Exception as e:
        info["SSL Error"] = str(e)

    return info