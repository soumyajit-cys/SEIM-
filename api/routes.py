from fastapi import APIRouter
from models.log_model import RawLog
from ingestion.ingest_service import process_log
from storage.elastic import search_logs, search_alerts

router = APIRouter()

@router.post("/ingest")
async def ingest(log: RawLog):
    await process_log(log)
    return {"status": "processed"}

@router.get("/logs")
async def get_logs():
    query = {"query": {"match_all": {}}}
    return await search_logs(query)

@router.get("/alerts")
async def get_alerts():
    query = {"query": {"match_all": {}}}
    return await search_alerts(query)