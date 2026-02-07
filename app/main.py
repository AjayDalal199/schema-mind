from fastapi import FastAPI

from app.core.config import settings
from app.api.health import router as health_router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

# Routers
app.include_router(health_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to SchemaMind API"
    }
