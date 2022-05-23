# Python
from typing import List, Optional

# Pydantic
from pydantic import BaseModel

# Base Cultivo List
class CultivoBase(BaseModel):
    id: int
    nom_cultivo: str
    class Config:
        orm_mode = True

# Mostrar Solo el nom_cultivo 
class Cultivo(CultivoBase):
    pass

# Mostrar nom_cultivo y Abreviatura_cultivo
class CultivoList(Cultivo):
    abreviatura_cultivo: Optional[str] = None
