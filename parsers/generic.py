from models.log_model import NormalizedLog

class GenericParser:
    async def parse(self, raw):
        return NormalizedLog(
            timestamp=raw.timestamp,
            host=raw.host,
            source=raw.source,
            event_type="generic",
            username=None,
            ip=None,
            status=None,
            message=raw.log
        )
    


    