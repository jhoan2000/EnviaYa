from fastapi import APIRouter
from models.usuario import UsuarioCreate
from services.usuario_service import crear_usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("")
def crear(usuario: UsuarioCreate):
    return{
        "mensaje": "Usuario creado",
        "data": crear_usuario(usuario)
    }