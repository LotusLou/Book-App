from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Book App"
    database_url: str = "sqlite:///./sqlite.db"


settings = Settings()
