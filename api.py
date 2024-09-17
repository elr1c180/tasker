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
def read_tariffs(db: Session = Depends(get_db)):
    return crud.get_tariffs(db)

@app.post("/tariffs/")
def create_tariff(name: str, price: float, is_active: bool = True, db: Session = Depends(get_db)):
    return crud.create_tariff(db, name, price, is_active)

@app.put("/tariffs/{tariff_id}")
def update_tariff(tariff_id: int, name: str = None, price: float = None, is_active: bool = None, db: Session = Depends(get_db)):
    tariff = crud.update_tariff(db, tariff_id, name, price, is_active)
    if tariff is None:
        raise HTTPException(status_code=404, detail="Tariff not found")
    return tariff

@app.delete("/tariffs/{tariff_id}")
def delete_tariff(tariff_id: int, db: Session = Depends(get_db)): 
    tariff = crud.delete_tariff(db, tariff_id)
    if tariff is None:
        raise HTTPException(status_code=404, detail="Tariff not found")
    return {"detail": "Tariff deleted"}
