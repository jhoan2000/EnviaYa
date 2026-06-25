from fastapi import HTTPException

from models.usuario import Usuario
from models.solicitud import Solicitud


class SolicitudService:

    @staticmethod
    def crear_solicitud(
        db,
        datos
    ):

        cliente = (
            db.query(Usuario)
            .filter(
                Usuario.id == datos.cliente_id
            )
            .first()
        )

        if not cliente:
            raise HTTPException(
                status_code=404,
                detail="Cliente no encontrado"
            )

        solicitud = Solicitud(
            cliente_id=datos.cliente_id,
            origen=datos.origen,
            destino=datos.destino,
            descripcion=datos.descripcion
        )

        db.add(solicitud)

        db.commit()

        db.refresh(solicitud)

        return solicitud