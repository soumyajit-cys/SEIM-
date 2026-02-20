from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RawLog(BaseModel):
    source: str
    host: str
    log: str
    timestamp: datetime

class NormalizedLog(BaseModel):
    timestamp: datetime
    host: str
    source: str
    event_type: Optional[str]
    username: Optional[str]
    ip: Optional[str]
    status: Optional[str]
    message: str
    