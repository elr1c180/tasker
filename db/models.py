from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey
from .core import Base
from sqlalchemy.orm import relationship

class Tariff(Base):
    __tablename__ = "tariffs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)


class Direction(Base):
    __tablename__ = "directions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    description = Column(Text)
    is_active = Column(Boolean, default=True)

    themes = relationship("Theme", back_populates="direction")

class Theme(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    direction_id = Column(Integer, ForeignKey("directions.id"))

    direction = relationship("Direction", back_populates="themes")