from sqlalchemy.orm import Session
from . import models

def get_tariffs(db: Session):
    return db.query(models.Tariff).all()

def get_tariff_by_name(db: Session, name: str):
    return db.query(models.Tariff).filter(models.Tariff.name == name).first()

def create_tariff(db: Session, name: str, price: float, is_active: bool):
    if get_tariff_by_name(db, name):
        raise ValueError("Tariff with this name already exists.")
    new_tariff = models.Tariff(name=name, price=price, is_active=is_active)
    db.add(new_tariff)
    db.commit()
    db.refresh(new_tariff)
    return new_tariff

def update_tariff(db: Session, name: str, new_name: str = None, price: float = None, is_active: bool = None):
    tariff = get_tariff_by_name(db, name)
    if tariff is None:
        raise ValueError("Tariff not found")
    if new_name is not None:
        tariff.name = new_name
    if price is not None:
        tariff.price = price
    if is_active is not None:
        tariff.is_active = is_active
    db.commit()
    db.refresh(tariff)
    return tariff

def delete_tariff(db: Session, name: str):
    tariff = get_tariff_by_name(db, name)
    if tariff is None:
        raise ValueError("Tariff not found")
    db.delete(tariff)
    db.commit()
    return tariff
