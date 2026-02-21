from models.alert_model import Alert
from storage.elastic import index_alert
from alerts.email_alert import send_email
from alerts.slack_alert import send_slack
from datetime import datetime

async def trigger_alert(severity, rule, ip, username, count):

    alert = Alert(
        severity=severity,
        rule=rule,
        ip=ip,
        username=username,
        count=count,
        timestamp=datetime.utcnow()
    )

    alert_dict = alert.dict()

    await index_alert(alert_dict)

    await send_email(alert_dict)
    await send_slack(alert_dict)