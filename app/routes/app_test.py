# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import status, HTTPException

# APP
from app.models.app_test import test
from app.schemas.app_test import Test
from app.config.db import conn


t = APIRouter()

## Listar todos los tests
@t.get(
    path="/tests",
    response_model=List[Test],
    status_code=status.HTTP_200_OK,
    summary="Listar todos los tests",
    tags=["tests"]
    )
def get_test():
    """
    Listar todos los tests
    """
    query = conn.execute(test.select()).fetchall()
    if query:
        return query
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay tests")


## Mostrar test por id
@t.get(
    path="/tests/{id}",
    response_model=Test,
    status_code=status.HTTP_200_OK,
    summary="Listar tests por id",
    tags=["tests"]
    )
def get_test_by_id(id: str):
    """
    Lista el test por id
    """
    query = conn.execute(test.select().where(test.c.id == id)).fetchone()
    if query:
        return query
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Test no encontrado")


## Crear test
@t.post(
    path="/tests",
    response_model=Test,
    status_code=status.HTTP_201_CREATED,
    summary="Crear test",
    tags=["tests"]
    )
def create_test(testbody: Test):
    """
    Crear test
    """

    query = conn.execute(test.insert().values(
        cultivo=testbody.cultivo,
        fundo=testbody.fundo,
        dni=testbody.dni
    ))
    if query:
        return conn.execute(test.select().where(test.c.id == query.lastrowid)).first()
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error al crear test")

## Actualizar test
@t.put(
    path="/tests/{id}",
    response_model=Test,
    status_code=status.HTTP_200_OK,
    summary="Actualizar test",
    tags=["tests"]
    )
def update_test(id: str, testbody: Test):
    """
    Actualizar test
    """
    query = conn.execute(test.update().where(test.c.id == id).values(
        cultivo=testbody.cultivo,
        fundo=testbody.fundo,
        dni=testbody.dni
    ))
    if query:
        return conn.execute(test.select().where(test.c.id == id)).first()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Test no encontrado")

## Eliminar test
@t.delete(
    path="/tests/{id}",
    status_code=status.HTTP_200_OK,
    summary="Eliminar test",
    tags=["tests"]
    )
def delete_test(id: str):
    """
    Eliminar test
    """
    # query = 
    query = conn.execute(test.select().where(test.c.id == id)).first()
    if query:
        conn.execute(test.delete().where(test.c.id == id))
        return {"detail": "Test {} eliminado".format(id)}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Test no encontrado")

