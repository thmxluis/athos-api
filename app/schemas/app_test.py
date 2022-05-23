# Python
from typing import List, Optional

# Pydantic
from pydantic import BaseModel

# Base Test List
class TestBase(BaseModel):
    class Config:
        orm_mode = True

# Mostrar los tests 
class Test(TestBase):
    id: Optional[int]
    fundo: Optional[str] = None
    cultivo: Optional[str] = None
    dni: Optional[str] = None


