import smtplib
from email.mime.text import MIMEText
from config.settings import settings

async def send_email(alert):

    if not settings.SMTP_USER:
        return

    body = f"""
    SIEM Alert Triggered

    Rule: {alert['rule']}
    Severity: {alert['severity']}
    IP: {alert['ip']}
    User: {alert['username']}
    Count: {alert['count']}
    """

    msg = MIMEText(body)
    msg["Subject"] = f"[SIEM] {alert['severity']} Alert"
    msg["From"] = settings.SMTP_USER
    msg["To"] = settings.SMTP_USER

    server = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
    server.starttls()
    server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
    server.send_message(msg)
    server.quit()