from sqlalchemy import Column, Integer, String, Float, Boolean
from .core import Base

class Tariff(Base):
    __tablename__ = "tariffs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
