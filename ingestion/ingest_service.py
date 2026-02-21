from parsers.linux_auth import LinuxAuthParser
from parsers.apache import ApacheParser
from parsers.generic import GenericParser
from storage.elastic import index_log
from detection.rule_engine import process_event

linux_parser = LinuxAuthParser()
apache_parser = ApacheParser()
generic_parser = GenericParser()

async def process_log(raw_log):
    parser = {
        "linux-auth": linux_parser,
        "apache": apache_parser
    }.get(raw_log.source, generic_parser)

    parsed = await parser.parse(raw_log)

    if parsed:
        log_dict = parsed.dict()
        await index_log(log_dict)
        await process_event(log_dict)