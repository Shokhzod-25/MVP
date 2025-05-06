from fastapi import FastAPI

from app.handlers.router import router


def create_app():
    app = FastAPI()
    app.include_router(router=router)

    return app
