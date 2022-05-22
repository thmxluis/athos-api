# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import status, HTTPException

# APP
from app.models.cultivo import cultivo
from app.schemas.cultivo import Cultivo, CultivoList
from app.config.db import conn


cul = APIRouter()

## Listar todos los cultivos
@cul.get(
    path="/cultivos",
    response_model=List[Cultivo],
    status_code=status.HTTP_200_OK,
    summary="Listar todos los cultivos",
    tags=["cultivos"]
    )
def get_cultivo():
    """
    Lis todos los cultivos
    """
    query = conn.execute(cultivo.select()).fetchall()
    if query:
        return query
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay cultivos")


## Mostrar Cultivo por nom_cultivo
@cul.get(
    path="/cultivos/{nom_cultivo}",
    response_model=CultivoList,
    status_code=status.HTTP_200_OK,
    summary="Listar cultivos por nom_cultivo",
    tags=["cultivos"]
    )
def get_cultivo_by_nom_cultivo(nom_cultivo: str):
    """
    Lista el cultivo por nom_cultivo
    """
    query = conn.execute(cultivo.select().where(cultivo.c.nom_cultivo == nom_cultivo)).fetchone()
    if query:
        return query
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cultivo no encontrado")






