from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="SIEM-Lite")

app.include_router(router)