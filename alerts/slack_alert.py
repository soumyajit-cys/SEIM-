import httpx
from config.settings import settings

async def send_slack(alert):

    if not settings.SLACK_WEBHOOK:
        return

    payload = {
        "text": f"""
        🚨 *SIEM Alert*
        Rule: {alert['rule']}
        Severity: {alert['severity']}
        IP: {alert['ip']}
        User: {alert['username']}
        Count: {alert['count']}
        """
    }

    async with httpx.AsyncClient() as client:
        await client.post(settings.SLACK_WEBHOOK, json=payload)