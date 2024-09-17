from sqlalchemy.orm import Session
from . import models

def get_tariffs(db: Session):
    return db.query(models.Tariff).all()

def create_tariff(db: Session, name: str, price: float, is_active: bool):
    new_tariff = models.Tariff(name=name, price=price, is_active=is_active)
    db.add(new_tariff)
    db.commit()
    db.refresh(new_tariff)
    return new_tariff

def update_tariff(db: Session, tariff_id: int, name: str = None, price: float = None, is_active: bool = None):
    tariff = db.query(models.Tariff).filter(models.Tariff.id == tariff_id).first()
    if name:
        tariff.name = name
    if price:
        tariff.price = price
    if is_active is not None:
        tariff.is_active = is_active
    db.commit()
    db.refresh(tariff)
    return tariff

def delete_tariff(db: Session, tariff_id: int):
    tariff = db.query(models.Tariff).filter(models.Tariff.id == tariff_id).first()
    db.delete(tariff)
    db.commit()
