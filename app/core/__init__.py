from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

load_dotenv()
#carregamos as variáveis de ambiente do arquivo .env.dev usando a função load_dotenv do pacote python-dotenv. Isso permite que as variáveis de ambiente sejam acessadas no código usando os métodos do Pydantic.
class Settings(BaseSettings):
    APP_NAME: str
    ENVIRONMENT: str
    DEBUG: bool
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(env_file=".env.dev",env_file_encoding="utf-8")

settings = Settings()