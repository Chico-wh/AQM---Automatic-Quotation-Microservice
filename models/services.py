from core.database import Base
from sqlalchemy import Column, Float, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, mapped_column ,Mapped
from datetime import datetime
from models.user import User

class Services(Base):
    __tablename__ = "services"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    name :Mapped[str] = mapped_column(String, nullable=False)
    description : Mapped[str] = mapped_column(String, nullable=True)
    price : Mapped[float] = mapped_column(Float, nullable=False)
    #relacionamento com o usuário, indicando que cada serviço pertence a um usuário específico. O back_populates é usado para criar uma relação bidirecional entre os modelos, permitindo acessar os serviços de um usuário e o usuário de um serviço.
    user: Mapped["User"] = relationship(
        "User", back_populates="services"
    )
    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

