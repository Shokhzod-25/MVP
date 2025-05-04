from uvicorn import run
from app import create_app
from app.core.config import settings

if __name__ == "__main__":
    run(
        "main:create_app",
        reload=True,
        factory=True,
        host=settings.HOST,
        port=settings.PORT,
    )
