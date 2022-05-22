# Python
from typing import List

# Pydantic
# ------------------------------------------------------------------------------

# FastAPI
from fastapi import APIRouter

# APP
from app.models.personal import personal
from app.schemas.personal import Personal
from app.config.db import conn


per = APIRouter()

## Listar todo el Personal
@per.get(
    path="/personal",
    response_model=List[Personal],
    summary="Get all personal",
    description="Get all personal",
    tags=["personal"]
    )
def get_personal():
    """
    Get all personal
    """
    return conn.execute(personal.select()).fetchall()


## Listar Personal por Nro_Doc
@per.get(
    path="/personal/{Nro_Doc}",
    response_model=Personal,
    summary="Get personal by Nro_Doc",
    description="Get personal by Nro_Doc",
    tags=["personal"]
    )
def get_personal_by_Nro_Doc(Nro_Doc: str):
    """
    Get personal by Nro_Doc
    """
    return conn.execute(personal.select().where(personal.c.Nro_Doc == Nro_Doc)).fetchone()





