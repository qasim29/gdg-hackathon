from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="GDG API", version="0.1.0")


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "gdg-api"
    }
