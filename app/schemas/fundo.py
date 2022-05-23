# Python
from typing import List, Optional

# Pydantic
from pydantic import BaseModel

# Base Fundo List
class FundoBase(BaseModel):
    id: int
    nom_fundo: str
    class Config:
        orm_mode = True

# Mostrar Solo el nom_Fundo 
class Fundo(FundoBase):
    pass

# Mostrar nom_Fundo y empresa
class FundoList(Fundo):
    empresa: Optional[str] = None
