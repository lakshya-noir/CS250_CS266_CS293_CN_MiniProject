from banner import grab_banner
from identifier import identify_server
from ssl_info import get_ssl_info
from utils import resolve_host, measure_latency

def fingerprint(target, port):
    print("=" * 60)
    print(f"Target: {target}")
    print(f"Port: {port}")

    ip = resolve_host(target)
    print(f"IP: {ip}")

    latency = measure_latency(target, port)
    print(f"Latency: {latency} ms")

    print("\n--- Banner Information ---")
    banner = grab_banner(target, port)

    if banner:
        print(banner)

    print("\n--- Server Identification ---")
    server = identify_server(banner)
    print(server)

    if port == 443:
        print("\n--- SSL Information ---")
        ssl_data = get_ssl_info(target, port)
        for k, v in ssl_data.items():
            print(f"{k}: {v}")

    print("=" * 60)


if __name__ == "__main__":
    targets = [
        ("google.com", 443),
        ("example.com", 80),
        ("github.com", 443)
    ]

    for t, p in targets:
        fingerprint(t, p)