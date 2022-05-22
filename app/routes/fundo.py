# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import status, HTTPException

# APP
from app.models.fundo import fundo
from app.schemas.fundo import Fundo, FundoList
from app.config.db import conn


fun = APIRouter()

## Listar todos los fundos
@fun.get(
    path="/fundos",
    response_model=List[Fundo],
    status_code=status.HTTP_200_OK,
    summary="Listar todos los fundos",
    tags=["fundos"]
    )
def get_fundo():
    """
    Listar todos los fundos
    """
    query = conn.execute(fundo.select()).fetchall()
    if query:
        return query
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay fundos")


## Mostrar fundo por nom_fundo
@fun.get(
    path="/fundos/{nom_fundo}",
    response_model=FundoList,
    status_code=status.HTTP_200_OK,
    summary="Listar fundos por nom_fundo",
    tags=["fundos"]
    )
def get_fundo_by_nom_fundo(nom_fundo: str):
    """
    Lista el fundo por nom_fundo
    """
    query = conn.execute(fundo.select().where(fundo.c.nom_fundo == nom_fundo)).fetchone()

    if query:
        return query
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fundo no encontrado")







