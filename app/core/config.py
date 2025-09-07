from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./todo.db"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()
