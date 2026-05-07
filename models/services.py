from core.database import Base
from sqlalchemy import Column, Float, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, mapped_column ,Mapped
from datetime import datetime

class Services(Base):
    __tablename__ = "services"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    name :Mapped[str] = mapped_column(String, nullable=False)
    description : Mapped[str] = mapped_column(String, nullable=True)
    price : Mapped[float] = mapped_column(Float, nullable=False)
    #relacionamento com o usuário, indicando que cada serviço pertence a um usuário específico. O back_populates é usado para criar uma relação bidirecional entre os modelos, permitindo acessar os serviços de um usuário e o usuário de um serviço.
    #declarei user_id como uma chave estrangeira que referencia a tabela users, garantindo a integridade referencial entre os serviços e os usuários. O relacionamento com o modelo User é estabelecido usando a função relationship do SQLAlchemy, permitindo acessar o usuário associado a cada serviço.
    user: Mapped["User"] = relationship(
        "User", back_populates="services"
    )
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    quote: Mapped[list["Quote"]] = relationship("Quote", back_populates="service")
    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

