import os
from pydantic_settings import BaseSettings, SettingsConfigDict

# Application Settings
class Settings(BaseSettings):
    DATABASE_URL: str = os.environ.get("DATABASE_URL")


    # Pydantic Settings Config, with this file we don't need python-dotenv package
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()