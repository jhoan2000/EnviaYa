from fastapi import FastAPI

from database.base import Base
from database.connection import engine

from models.usuario import Usuario
from models.domiciliario import Domiciliario

from api.usuario import router as usuario_router

from api.domiciliario import router as domiciliario_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(usuario_router)
app.include_router(domiciliario_router)

@app.get("/")
def home():
    return {"mensaje": "Hola"}