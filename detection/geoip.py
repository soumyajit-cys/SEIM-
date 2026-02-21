def lookup_ip(ip: str):
    # Mock geo lookup
    if ip.startswith("10.") or ip.startswith("192.168"):
        return "Private Network"
    return "Unknown Country"