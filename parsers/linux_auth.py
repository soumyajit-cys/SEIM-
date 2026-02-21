import re
from models.log_model import NormalizedLog

FAILED_REGEX = r"Failed password for (\w+) from ([\d\.]+)"

class LinuxAuthParser:
    async def parse(self, raw):
        match = re.search(FAILED_REGEX, raw.log)

        if match:
            return NormalizedLog(
                timestamp=raw.timestamp,
                host=raw.host,
                source=raw.source,
                event_type="login_attempt",
                username=match.group(1),
                ip=match.group(2),
                status="failed",
                message=raw.log
            )

        return None