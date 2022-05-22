# Python
from typing import List, Optional

# Pydantic
from pydantic import BaseModel


class Personal(BaseModel):
    Nro_Doc: str
    Nombres: str
    Apellido_Pat: str
    Apellido_Mat: str

