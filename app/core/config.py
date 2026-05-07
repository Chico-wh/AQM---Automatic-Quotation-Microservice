from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os
#carregamos as variáveis de ambiente do arquivo .env.dev usando a função load_dotenv do pacote python-dotenv. Isso permite que as variáveis de ambiente sejam acessadas no código usando os métodos do Pydantic.
class Settings(BaseSettings):
    #definimos a classe Settings que herda de BaseSettings do Pydantic. Esta classe contém os campos de configuração da aplicação, como o nome da aplicação, ambiente, debug, URL do banco de dados, chave secreta, algoritmo de criptografia e tempo de expiração do token de acesso.
    #so e Permitida declarações de tipos
    APP_NAME: str
    ENVIRONMENT: str
    DEBUG: bool
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(env_file=".env.example",env_file_encoding="utf-8")

settings = Settings()