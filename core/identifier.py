def identify_server(banner):
    if not banner:
        return "Unknown"

    banner = banner.lower()

    if "apache" in banner:
        return "Apache Web Server"

    if "nginx" in banner:
        return "Nginx Web Server"

    if "iis" in banner:
        return "Microsoft IIS"

    if "cloudflare" in banner:
        return "Cloudflare"

    if "gws" in banner:
        return "Google Web Server"

    if "envoy" in banner:
        return "Envoy Proxy"

    return "Unknown Server"