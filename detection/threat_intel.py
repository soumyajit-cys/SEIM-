KNOWN_BAD_IPS = {"8.8.8.8": "Known scanner"}

def check_threat_intel(ip):
    return KNOWN_BAD_IPS.get(ip)