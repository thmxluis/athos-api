
# Sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.sql.sqltypes import Integer, String

# APP   
from app.config.db import meta, engine


test = Table(
    'app_test', meta,
    Column('id', Integer, primary_key=True),
    Column('fundo', String(100), nullable=True),
    Column('cultivo', String(100), nullable=True),
    Column('dni', String(100), nullable=True)
)
