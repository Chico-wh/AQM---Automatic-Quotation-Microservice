#importamos o BaseModel do Pydantic para criar um modelo de dados para o usuário
#Os tipos do sqlalchemy pra tipos(importante)
from pydantic import BaseModel
from datetime import date, datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship,Mapped,mapped_column
from core.database import Base
from models.customers import Customer
from models.services import Services
from models.quote import Quote
from models.pricing_rule import Rule
#mapped serve pra tipar colunas do sqlalchemy, e mapped_column é usado para definir as colunas do modelo de dados. Esses imports são necessários para criar a classe User que representa um usuário no banco de dados, com campos como username, password e is_active.

#criamos a classe User que herda de BaseModel, com os campos username e password, ambos do tipo string. Este modelo será usado para validar os dados de entrada ao criar um novo usuário ou fazer login.

class User(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    hash_password: Mapped[str] = mapped_column(String, nullable=False)
    #relacionamento com clientes e serviços, indicando que um usuário pode ter vários clientes e serviços associados a ele. O back_populates é usado para criar uma relação bidirecional entre os modelos, permitindo acessar os clientes e serviços de um usuário e o usuário de um cliente ou serviço.
    clients:Mapped[list["Customer"]] = relationship("Customer", back_populates="user")
    #relacionamento com regras de precificação, indicando que um usuário pode ter várias regras de precificação associadas a ele. O back_populates é usado para criar uma relação bidirecional entre os modelos, permitindo acessar as regras de precificação de um usuário e o usuário de uma regra.
    
    services:Mapped[list["Services"]] = relationship("Services", back_populates="user")
    quotes:Mapped[list["Quote"]] = relationship("Quote", back_populates="user")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    customer :Mapped[Customer] = relationship("Customer", back_populates="user")
    created_at :Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), nullable=False)
    