from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "SIEM-Lite"

    ELASTIC_HOST: str = "http://elasticsearch:9200"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379

    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""

    SLACK_WEBHOOK: str = ""

    BLACKLISTED_IPS: str = "10.0.0.5,192.168.1.200"

    class Config:
        env_file = ".env"

settings = Settings()