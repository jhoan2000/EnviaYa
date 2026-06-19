from fastapi import APIRouter, HTTPException
from models.auth import LoginRequest
from services.usuario_service import login_usuario

router = APIRouter(tags=["Auth"])

@router.post("/login")
def login(data: LoginRequest):
    user = login_usuario(data.correo, data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    return {"mensaje": "Login exitoso"}
