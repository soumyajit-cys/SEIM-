from pydantic import BaseModel
from datetime import datetime

class Alert(BaseModel):
    severity: str
    rule: str
    ip: str | None
    username: str | None
    count: int | None
    timestamp: datetime

    