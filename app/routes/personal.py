# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import status

# APP
from app.models.personal import personal
from app.schemas.personal import Personal, PersonalList
from app.config.db import conn


per = APIRouter()

## Listar todo el Personal
@per.get(
    path="/personal",
    response_model=List[Personal],
    status_code=status.HTTP_200_OK,
    summary="Listar todo el personal",
    tags=["personal"]
    )
def get_personal():
    """
    Lis todo el personal, solo el Nro_Doc
    """
    return conn.execute(personal.select()).fetchall()


## Listar Personal por Nro_Doc
@per.get(
    path="/personal/{Nro_Doc}",
    response_model=PersonalList,
    status_code=status.HTTP_200_OK,
    summary="Listar personal por Nro_Doc",
    tags=["personal"]
    )
def get_personal_by_Nro_Doc(Nro_Doc: str):
    """
    Lista el personal por Nro_Doc con su nombr y apellidos.
    """
    return conn.execute(personal.select().where(personal.c.Nro_Doc == Nro_Doc)).fetchone()





