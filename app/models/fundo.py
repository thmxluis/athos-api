
# Sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.sql.sqltypes import Integer, String

# APP   
from app.config.db import meta, engine


fundo = Table(
    'menu_fundo', meta,
    Column('id', Integer, primary_key=True),
    Column('nom_fundo', String(100), nullable=True),
    Column('empresa', String(100), nullable=True)
)
