import json
from datetime import datetime
from storage.redis_client import redis_client
from detection.rules import RULES
from alerts.alert_engine import trigger_alert
from config.settings import settings

BLACKLIST = settings.BLACKLISTED_IPS.split(",")

async def process_event(event: dict):

    for rule in RULES:

        # Event type filtering
        if rule["event_type"] != "*" and event.get("event_type") != rule["event_type"]:
            continue

        # Condition filtering
        for key, value in rule["condition"].items():
            if event.get(key) != value:
                continue

        # Blacklist rule (special case)
        if rule["rule_name"] == "Blacklisted IP Access":
            if event.get("ip") in BLACKLIST:
                await trigger_alert(
                    severity=rule["severity"],
                    rule=rule["rule_name"],
                    ip=event.get("ip"),
                    username=event.get("username"),
                    count=1
                )
            continue

        # Redis sliding window counter
        key = f"{rule['rule_name']}:{event.get('ip')}:{event.get('username')}"
        current_count = await redis_client.incr(key)

        if current_count == 1:
            await redis_client.expire(key, rule["time_window"])

        if current_count >= rule["threshold"]:
            await trigger_alert(
                severity=rule["severity"],
                rule=rule["rule_name"],
                ip=event.get("ip"),
                username=event.get("username"),
                count=current_count
            )

            # reset counter after alert
            await redis_client.delete(key)