
# Sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.sql.sqltypes import Integer, String

# APP   
from app.config.db import meta, engine


cultivo = Table(
    'menu_cultivo', meta,
    Column('id', Integer, primary_key=True),
    Column('nom_cultivo', String(100), nullable=True),
    Column('abreviatura_cultivo', String(100), nullable=True)
)
