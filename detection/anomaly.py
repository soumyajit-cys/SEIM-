import statistics
from storage.redis_client import redis_client
from alerts.alert_engine import trigger_alert
from datetime import datetime

WINDOW_SIZE = 20
Z_THRESHOLD = 3

async def detect_anomaly(metric_key: str, value: int, metadata: dict):

    history_key = f"anomaly:{metric_key}"

    # Store historical values
    await redis_client.rpush(history_key, value)
    await redis_client.ltrim(history_key, -WINDOW_SIZE, -1)

    history = await redis_client.lrange(history_key, 0, -1)
    history = list(map(int, history))

    if len(history) < 5:
        return

    mean = statistics.mean(history)
    std_dev = statistics.stdev(history) if len(history) > 1 else 0

    if std_dev == 0:
        return

    z_score = (value - mean) / std_dev

    if abs(z_score) >= Z_THRESHOLD:
        await trigger_alert(
            severity="medium",
            rule="Anomalous Activity Spike",
            ip=metadata.get("ip"),
            username=metadata.get("username"),
            count=value
        )