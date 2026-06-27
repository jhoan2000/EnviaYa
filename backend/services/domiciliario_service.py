from models.domiciliario import Domiciliario
from models.usuario import Usuario

from fastapi import HTTPException

from utils.validaciones import obtener_usuario, obtener_domiciliario
from utils.permisos import validar_domiciliario

class DomiciliarioService:

    @staticmethod
    def crear_domiciliario(
        db,
        datos
    ):
        usuario = obtener_usuario(
            db,
            datos.usuario_id
        )

        validar_domiciliario(usuario)

        domiciliario = Domiciliario(
            usuario_id=datos.usuario_id,
            vehiculo=datos.vehiculo,
            placa=datos.placa
        )

        db.add(domiciliario)

        db.commit()

        db.refresh(domiciliario)

        return domiciliario