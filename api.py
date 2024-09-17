from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, crud, core
from db.core import get_db
from typing import AsyncGenerator

async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Выполнение при старте приложения
    models.Base.metadata.create_all(bind=core.engine)
    yield
    # Выполнение при завершении

app = FastAPI(lifespan=lifespan)

@app.get("/tariffs/")
async def read_tariffs(db: Session = Depends(get_db)):
    return crud.get_tariffs(db)

@app.post("/tariffs/")
async def create_tariff(name: str, price: float, is_active: bool = True, db: Session = Depends(get_db)):
    return crud.create_tariff(db, name, price, is_active)

@app.put("/tariffs/{tariff_id}")
async def update_tariff(tariff_id: int, name: str = None, price: float = None, is_active: bool = None, db: Session = Depends(get_db)):
    return crud.update_tariff(db, tariff_id, name, price, is_active)

@app.delete("/tariffs/{tariff_id}")
async def delete_tariff(tariff_id: int, db: Session = Depends(get_db)):
    return crud.delete_tariff(db, tariff_id)

@app.get("/directions/")
async def read_directions(db: Session = Depends(get_db)):
    return crud.get_directions(db)

@app.get("/directions/{direction_id}/themes/")
async def read_themes_by_direction(direction_id: int, db: Session = Depends(get_db)):
    return crud.get_themes_by_direction(db, direction_id)

@app.post("/directions/")
async def create_direction(name: str, description: str, is_active: bool = True, db: Session = Depends(get_db)):
    return crud.create_direction(db, name, description, is_active)

@app.post("/themes/")
async def create_theme(name: str, description: str, direction_id: int, is_active: bool = True, db: Session = Depends(get_db)):
    return crud.create_theme(db, name, description, is_active, direction_id)

@app.put("/directions/{direction_id}")
async def update_direction(direction_id: int, name: str = None, description: str = None, is_active: bool = None, db: Session = Depends(get_db)):
    direction = crud.update_direction(db, direction_id, name, description, is_active)
    if direction is None:
        raise HTTPException(status_code=404, detail="Direction not found")
    return direction

@app.put("/themes/{theme_id}")
async def update_theme(theme_id: int, name: str = None, description: str = None, is_active: bool = None, db: Session = Depends(get_db)):
    theme = crud.update_theme(db, theme_id, name, description, is_active)
    if theme is None:
        raise HTTPException(status_code=404, detail="Theme not found")
    return theme

@app.delete("/directions/{direction_id}")
async def delete_direction(direction_id: int, db: Session = Depends(get_db)):
    direction = crud.delete_direction(db, direction_id)
    if direction is None:
        raise HTTPException(status_code=404, detail="Direction not found")
    return {"detail": "Direction deleted"}

@app.delete("/themes/{theme_id}")
async def delete_theme(theme_id: int, db: Session = Depends(get_db)):
    theme = crud.delete_theme(db, theme_id)
    if theme is None:
        raise HTTPException(status_code=404, detail="Theme not found")
    return {"detail": "Theme deleted"}
