"""Main module."""
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import api
from app.api.v1.endpoints import generator
from app.core.config import config as c
from app.core.loggers import setup_logging

setup_logging(
    log_level=c.LOG_LEVEL, use_basic_format=c.LOG_USE_BASIC_FORMAT
)
_LOGGER = logging.getLogger(__name__)

app = FastAPI(
    docs_url=f"{c.API_PREFIX}/{api.__version__}/docs",
    openapi_url=f"{c.API_PREFIX}/{api.__version__}/openapi.json",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generator.router, prefix=c.API_PREFIX)


@app.get(f"{c.API_PREFIX}/{api.__version__}/health")
async def health_check():
    """Health check endpoint for the service"""
    return {"status": "healthy"}


@app.get(f"{c.API_PREFIX}/{api.__version__}/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "Resume Generator API",
        "endpoints": {
            "/": "API information",
            "/health": "Health check endpoint",
            "/resume/generate": "Generate a PDF resume (POST)"
        }
    }
