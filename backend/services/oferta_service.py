from fastapi import HTTPException

from models.oferta import Oferta
from models.solicitud import Solicitud
from models.domiciliario import Domiciliario

from utils.estados import EstadoOferta, EstadoSolicitud
from utils.validaciones import obtener_solicitud, obtener_domiciliario
from utils.permisos import validar_solicitud_abierta, validar_domiciliario_disponible
class OfertaService:

    @staticmethod
    def crear_oferta(
        db,
        datos
    ):
        solicitud = obtener_solicitud(
            db,
            datos.solicitud_id
        )
        validar_solicitud_abierta(solicitud)
        domiciliario = obtener_domiciliario(
            db,
            datos.domiciliario_id
        )
        validar_domiciliario_disponible(domiciliario)
        
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
    @staticmethod
    def aceptar_oferta(
        db,
        oferta_id
    ):
        
        oferta = (
            db.query(Oferta)
            .filter(Oferta.id == oferta_id)
            .first()
        )

        if not oferta:
            raise HTTPException(
                status_code=404,
                detail="Oferta no encontrada"
            )

        if oferta.estado != EstadoOferta.PENDIENTE:
            raise HTTPException(
                status_code=400,
                detail="La oferta ya fue procesada."
            )

        solicitud = (
            db.query(Solicitud)
            .filter(
                Solicitud.id == oferta.solicitud_id
            )
            .first()
        )

        oferta.estado = EstadoOferta.ACEPTADA

        solicitud.estado = EstadoSolicitud.ACEPTADA

        otras_ofertas = (
            db.query(Oferta)
            .filter(
                Oferta.solicitud_id == solicitud.id,
                Oferta.id != oferta.id
            )
            .all()
        )

        for otra in otras_ofertas:
            otra.estado = EstadoOferta.RECHAZADA

        db.commit()

        db.refresh(oferta)

        return oferta