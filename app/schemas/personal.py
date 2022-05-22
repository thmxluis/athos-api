# Python
from typing import List, Optional

# Pydantic
from pydantic import BaseModel

# Base Personal List
class PersonalBase(BaseModel):
    Nro_Doc: str

# Mostrar Solo el Nro_Doc 
class Personal(PersonalBase):
    pass

# Mostrar Nro_Doc y Nombres
class PersonalList(Personal):
    Nombres: Optional[str] = None
    Apellido_Pat: Optional[str] = None
    Apellido_Mat: Optional[str] = None
