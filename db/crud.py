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


def get_directions(db: Session):
    return db.query(models.Direction).all()

def get_themes_by_direction(db: Session, direction_id: int):
    return db.query(models.Theme).filter(models.Theme.direction_id == direction_id).all()

def create_direction(db: Session, name: str, description: str, is_active: bool):
    direction = models.Direction(name=name, description=description, is_active=is_active)
    db.add(direction)
    db.commit()
    db.refresh(direction)
    return direction

def create_theme(db: Session, name: str, description: str, is_active: bool, direction_id: int):
    theme = models.Theme(name=name, description=description, is_active=is_active, direction_id=direction_id)
    db.add(theme)
    db.commit()
    db.refresh(theme)
    return theme

def update_direction(db: Session, direction_id: int, name: str = None, description: str = None, is_active: bool = None):
    direction = db.query(models.Direction).filter(models.Direction.id == direction_id).first()
    if direction is None:
        return None
    if name is not None:
        direction.name = name
    if description is not None:
        direction.description = description
    if is_active is not None:
        direction.is_active = is_active
    db.commit()
    db.refresh(direction)
    return direction

def update_theme(db: Session, theme_id: int, name: str = None, description: str = None, is_active: bool = None):
    theme = db.query(models.Theme).filter(models.Theme.id == theme_id).first()
    if theme is None:
        return None
    if name is not None:
        theme.name = name
    if description is not None:
        theme.description = description
    if is_active is not None:
        theme.is_active = is_active
    db.commit()
    db.refresh(theme)
    return theme

def delete_direction(db: Session, direction_id: int):
    direction = db.query(models.Direction).filter(models.Direction.id == direction_id).first()
    if direction is None:
        return None
    db.delete(direction)
    db.commit()
    return direction

def delete_theme(db: Session, theme_id: int):
    theme = db.query(models.Theme).filter(models.Theme.id == theme_id).first()
    if theme is None:
        return None
    db.delete(theme)
    db.commit()
    return theme