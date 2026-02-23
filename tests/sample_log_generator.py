import requests
from datetime import datetime
import time

URL = "http://localhost:8000/ingest"

def send_failed_login(ip, user):
    payload = {
        "source": "linux-auth",
        "host": "192.168.1.10",
        "log": f"Failed password for {user} from {ip} port 22",
        "timestamp": datetime.utcnow().isoformat()
    }
    requests.post(URL, json=payload)

if __name__ == "__main__":

    attacker_ip = "10.0.0.5"

    for i in range(6):
        send_failed_login(attacker_ip, "root")
        time.sleep(1)

    print("Brute force simulation completed.")