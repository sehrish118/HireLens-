from fastapi import FastAPI

from app.api import health
from app.core.config import get_settings
from app.core.exceptions import add_exception_handlers
from app.core.logging import setup_logging

setup_logging()
settings = get_settings()

app = FastAPI(title=settings.app_name)
add_exception_handlers(app)
app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "API is running"}
