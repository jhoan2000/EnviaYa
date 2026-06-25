from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from schemas.usuario_schema import (
    UsuarioCreate,
    UsuarioResponse
)


from services.usuario_service import UsuarioService

from database.dependencias import get_db

from schemas.usuario_schema import UsuarioUpdate

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

@router.get(
    "/{usuario_id}",
    response_model=UsuarioResponse
)
def obtener_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):

    return UsuarioService.obtener_usuario(
        db,
        usuario_id
    )

@router.put(
    "/{usuario_id}",
    response_model=UsuarioResponse
)
def actualizar_usuario(
    usuario_id: int,
    datos: UsuarioUpdate,
    db: Session = Depends(get_db)
):

    return UsuarioService.actualizar_usuario(
        db,
        usuario_id,
        datos
    )