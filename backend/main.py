from fastapi import FastAPI
from api import usuarios, domiciliarios, auth

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(domiciliarios.router)
app.include_router(auth.router)