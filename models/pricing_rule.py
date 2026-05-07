from core.database import Base
from sqlalchemy import Column, Float, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, mapped_column ,Mapped
from datetime import datetime

class Rule(Base):
    __tablename__ = "pricing_rules"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    name :Mapped[str] = mapped_column(String, nullable=False)
    description : Mapped[str] = mapped_column(String, nullable=True)
    net_cost : Mapped[float] = mapped_column(Float, nullable=False)
    gross_cost : Mapped[float] = mapped_column(Float, nullable=False)
    #relacionamento com o usuário, indicando que cada regra de precificação pertence a um usuário específico. O back_populates é usado para criar uma relação bidirecional entre os modelos, permitindo acessar as regras de precificação de um usuário e o usuário de uma regra.
    #declarei user_id como uma chave estrangeira que referencia a tabela users, garantindo a integridade referencial entre as regras de precificação e os usuários. O relacionamento com o modelo User é estabelecido usando a função relationship do SQLAlchemy, permitindo acessar o usuário associado a cada regra.
    user: Mapped["User"] = relationship(
        "User", back_populates="pricing_rules"
    )
    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

