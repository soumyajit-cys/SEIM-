from models.log_model import NormalizedLog
import re

APACHE_REGEX = r'(\d+\.\d+\.\d+\.\d+).*"(GET|POST) (.*?)" (\d{3})'

class ApacheParser:
    async def parse(self, raw):
        match = re.search(APACHE_REGEX, raw.log)

        if match:
            return NormalizedLog(
                timestamp=raw.timestamp,
                host=raw.host,
                source=raw.source,
                event_type="http_request",
                username=None,
                ip=match.group(1),
                status=match.group(4),
                message=raw.log
            )

        return None