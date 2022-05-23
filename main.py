# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# APP
from app.routes.personal import per
from app.routes.cultivo import cul
from app.routes.fundo import fun
from app.routes.app_test import t

## Aplicacion
app = FastAPI(
    title="Athos API",
    description="a REST API using python and mysql",
    version="0.0.1"
)

## CORS
cors = CORSMiddleware(
    app,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## Rutas
app.include_router(per)
app.include_router(cul)
app.include_router(fun)
app.include_router(t)
