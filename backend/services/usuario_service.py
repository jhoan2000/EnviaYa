from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas import usuario_schema


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

        return db.query(Usuario).all()