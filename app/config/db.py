from sqlalchemy import create_engine, MetaData

engine = create_engine(
    url='mysql+pymysql://root@localhost:3306/athos0'
)

meta = MetaData()

conn = engine.connect()