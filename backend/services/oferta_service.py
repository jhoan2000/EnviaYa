from fastapi import HTTPException

from models.oferta import Oferta
from models.solicitud import Solicitud
from models.domiciliario import Domiciliario


class OfertaService:

    @staticmethod
    def crear_oferta(
        db,
        datos
    ):

        solicitud = (
            db.query(Solicitud)
            .filter(
                Solicitud.id == datos.solicitud_id
            )
            .first()
        )

        if not solicitud:
            raise HTTPException(
                status_code=404,
                detail="Solicitud no encontrada"
            )

        domiciliario = (
            db.query(Domiciliario)
            .filter(
                Domiciliario.id == datos.domiciliario_id
            )
            .first()
        )

        if not domiciliario:
            raise HTTPException(
                status_code=404,
                detail="Domiciliario no encontrado"
            )

        oferta = Oferta(
            solicitud_id=datos.solicitud_id,
            domiciliario_id=datos.domiciliario_id,
            valor=datos.valor,
            tiempo_estimado=datos.tiempo_estimado
        )

        db.add(oferta)

        db.commit()

        db.refresh(oferta)

        return oferta