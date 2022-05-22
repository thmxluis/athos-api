# Python

# Pydantic

# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# APP
from app.routes.personal import per
from app.routes.cultivo import cul


app = FastAPI(
    title="Athos API",
    description="a REST API using python and mysql",
    version="0.0.1"
)

app.include_router(per)
app.include_router(cul)
