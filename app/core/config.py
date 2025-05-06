from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///database.db"
    HOST: str = "0.0.0.0"
    PORT: int = 8005


settings = Settings()
