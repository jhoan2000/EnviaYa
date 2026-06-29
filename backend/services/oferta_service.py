from fastapi import HTTPException

from models.oferta import Oferta
from models.solicitud import Solicitud
from models.domiciliario import Domiciliario

from utils.estados import EstadoOferta, EstadoSolicitud
from utils.validaciones import (
    obtener_solicitud,
    obtener_domiciliario,
    obtener_oferta)
from utils.permisos import (
    validar_solicitud_abierta,
    validar_domiciliario_disponible,
    validar_oferta_pendiente,
    validar_solicitud_aceptada)
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
        
        oferta = obtener_oferta(db, oferta_id)
        
        validar_oferta_pendiente(oferta)
        
        solicitud = obtener_solicitud(
            db,
            oferta.solicitud_id
        )
        
        validar_solicitud_abierta(solicitud)

        domiciliario = obtener_domiciliario(
            db,
            oferta.domiciliario_id
        )
        oferta.estado = EstadoOferta.ACEPTADA
        solicitud.estado = EstadoSolicitud.ACEPTADA
        solicitud.domiciliario_id = oferta.domiciliario_id
        domiciliario.disponible = False
         
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