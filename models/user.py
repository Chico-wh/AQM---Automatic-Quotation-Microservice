#importamos o BaseModel do Pydantic para criar um modelo de dados para o usuário
#Os tipos do sqlalchemy pra tipos(importante)
from pydantic import BaseModel
from datetime import date, datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship,Mapped,mapped_column
from core.database import Base
#mapped serve pra tipar colunas do sqlalchemy, e mapped_column é usado para definir as colunas do modelo de dados. Esses imports são necessários para criar a classe User que representa um usuário no banco de dados, com campos como username, password e is_active.

#criamos a classe User que herda de BaseModel, com os campos username e password, ambos do tipo string. Este modelo será usado para validar os dados de entrada ao criar um novo usuário ou fazer login.

class User(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    hash_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at :Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), nullable=False)
    