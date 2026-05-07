from core.database import Base
from sqlalchemy import Column, Float, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, mapped_column ,Mapped
from datetime import datetime


class Quote(Base):
    __tablename__ = "quotes"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"), nullable=False)
    service: Mapped["Services"] = relationship("Services", back_populates="quote")
    description : Mapped[str] = mapped_column(String, nullable=True)
    net_cost : Mapped[float] = mapped_column(Float, nullable=False)
    gross_cost : Mapped[float] = mapped_column(Float, nullable=False)

    #relacionamento com o usuário, indicando que cada cotação pertence a um usuário específico. O back_populates é usado para criar uma relação bidirecional entre os modelos, permitindo acessar as cotações de um usuário e o usuário de uma cotação.
    #declarei user_id como uma chave estrangeira que referencia a tabela users, garantindo a integridade referencial entre as cotações e os usuários. O relacionamento com o modelo User é estabelecido usando a função relationship do SQLAlchemy, permitindo acessar o usuário associado a cada cotação.
    user: Mapped["User"] = relationship(
        "User", back_populates="quotes"
    )
    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

