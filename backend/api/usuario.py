from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from schemas.usuario_schema import (
    UsuarioCreate,
    UsuarioResponse
)


from services.usuario_service import UsuarioService

from database.dependencias import get_db


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


@router.post(
    "/",
    response_model=UsuarioResponse
)
def crear_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):

    return UsuarioService.crear_usuario(
        db,
        usuario
    )

@router.get(
    "/",
    response_model=list[UsuarioResponse]
)
def listar_usuarios(
    db: Session = Depends(get_db)
):

    return UsuarioService.listar_usuarios(db)