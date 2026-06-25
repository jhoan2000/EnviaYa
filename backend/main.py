from fastapi import FastAPI

from database.base import Base
from database.connection import engine

from models.usuario import Usuario
from models.domiciliario import Domiciliario
from models.solicitud import Solicitud

from api.usuario import router as usuario_router

from api.domiciliario import router as domiciliario_router

from api.solicitud import router as solicitud_router

from api.oferta import router as oferta_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(usuario_router)
app.include_router(domiciliario_router)
app.include_router(solicitud_router)
app.include_router(oferta_router)

@app.get("/")
def home():
    return {"mensaje": "Hola"}