
# Sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.sql.sqltypes import Integer, String

# APP   
from app.config.db import meta, engine


personal = Table(
    'rrhh_maestra_personal', meta,
    Column('Nro_Doc', String(100), nullable=True),
    Column('Nombres', String(100), nullable=True),
    Column('Apellido_Pat', String(100), nullable=True),
    Column('Apellido_Mat', String(100), nullable=True),
)
