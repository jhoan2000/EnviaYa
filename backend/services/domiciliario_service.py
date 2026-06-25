from models.domiciliario import Domiciliario
from models.usuario import Usuario

from fastapi import HTTPException


class DomiciliarioService:

    @staticmethod
    def crear_domiciliario(
        db,
        datos
    ):

        usuario = (
            db.query(Usuario)
            .filter(
                Usuario.id == datos.usuario_id
            )
            .first()
        )

        if not usuario:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )
        if usuario.rol != "domiciliario":
            raise HTTPException(
                status_code=400,
                detail="El usuario no tiene rol domiciliario"
            )
        domiciliario_existente = (
            db.query(Domiciliario)
            .filter(
                Domiciliario.usuario_id == datos.usuario_id
            )
            .first()
        )

        if domiciliario_existente:
            raise HTTPException(
                status_code=400,
                detail="El usuario ya tiene perfil de domiciliario"
            )

        domiciliario = Domiciliario(
            usuario_id=datos.usuario_id,
            vehiculo=datos.vehiculo,
            placa=datos.placa
        )

        db.add(domiciliario)

        db.commit()

        db.refresh(domiciliario)

        return domiciliario