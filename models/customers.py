from core.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship,mapped_column,Mapped
from datetime import datetime

class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="customer")
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)
