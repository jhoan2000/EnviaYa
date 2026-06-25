from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas import usuario_schema
from fastapi import HTTPException

from schemas.usuario_schema import (
    UsuarioCreate,
    UsuarioUpdate
)

from fastapi import HTTPException

class UsuarioService:

    @staticmethod
    def crear_usuario(db: Session, usuario: usuario_schema.UsuarioCreate):

        nuevo_usuario = Usuario(
            nombre=usuario.nombre,
            telefono=usuario.telefono,
            correo=usuario.correo,
            password_hash=usuario.password,  # temporal
            direccion_principal=usuario.direccion_principal
        )

        db.add(nuevo_usuario)

        db.commit()

        db.refresh(nuevo_usuario)

        return nuevo_usuario

    @staticmethod
    def listar_usuarios(db: Session):

        return (
        db.query(Usuario)
        .filter(Usuario.activo == True)
        .all()
    )
    
    @staticmethod
    def obtener_usuario(db, usuario_id: int):

        usuario = (
            db.query(Usuario)
            .filter(Usuario.id == usuario_id,
                    Usuario.activo == True)
            .first()
        )

        if not usuario:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

        return usuario
    
    @staticmethod
    def actualizar_usuario(
        db,
        usuario_id: int,
        datos: UsuarioUpdate
    ):

        usuario = (
            db.query(Usuario)
            .filter(Usuario.id == usuario_id)
            .first()
        )

        if not usuario:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

        if datos.nombre is not None:
            usuario.nombre = datos.nombre

        if datos.telefono is not None:
            usuario.telefono = datos.telefono

        if datos.direccion_principal is not None:
            usuario.direccion_principal = datos.direccion_principal

        db.commit()
        db.refresh(usuario)

        return usuario
    
    @staticmethod
    def desactivar_usuario(
        db,
        usuario_id: int
    ):

        usuario = (
            db.query(Usuario)
            .filter(Usuario.id == usuario_id)
            .first()
        )

        if not usuario:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

        usuario.activo = False

        db.commit()
        db.refresh(usuario)

        return usuario