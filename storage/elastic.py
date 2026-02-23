from elasticsearch import AsyncElasticsearch
from datetime import datetime
from config.settings import settings

es = AsyncElasticsearch(hosts=[settings.ELASTIC_HOST])

async def index_log(log: dict):
    index_name = f"logs-{datetime.utcnow().strftime('%Y-%m-%d')}"
    await es.index(index=index_name, document=log)

async def index_alert(alert: dict):
    await es.index(index="alerts", document=alert)

async def search_logs(query: dict):
    return await es.search(index="logs-*", body=query)

async def search_alerts(query: dict):
    return await es.search(index="alerts", body=query)


