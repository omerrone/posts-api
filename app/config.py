import os
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV_PATH = os.path.join(os.path.dirname(__file__), ".env")

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file=DOTENV_PATH, env_file_encoding="utf-8", case_sensitive=False)

try:
    settings = Settings()
except Exception as e:
    print(f"An error occurred: {e}")
    print(f"Attempted to load .env from: {DOTENV_PATH}")