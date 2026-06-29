from fastapi import HTTPException

from models.usuario import Usuario
from models.solicitud import Solicitud

from utils.estados import *
from utils.estados import EstadoOferta, EstadoSolicitud
from utils.validaciones import (
    obtener_solicitud,
    obtener_domiciliario)
from utils.permisos import (
    validar_solicitud_aceptada,
    validar_solicitud_en_curso,
    validar_domiciliario_asignado)

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
    @staticmethod
    def iniciar_servicio(
        db,
        solicitud_id,
        domiciliario_id
    ):

        solicitud = obtener_solicitud(
            db,
            solicitud_id,
        )

        validar_solicitud_aceptada(solicitud)

        validar_domiciliario_asignado(
            solicitud,
            domiciliario_id)

        solicitud.estado = EstadoSolicitud.EN_CURSO

        db.commit()

        db.refresh(solicitud)

        return solicitud
    @staticmethod
    def finalizar_servicio(
        db,
        solicitud_id,
        domiciliario_id
    ):
        solicitud = obtener_solicitud(
            db,
            solicitud_id
        )

        validar_solicitud_en_curso(
            solicitud
        )

        validar_domiciliario_asignado(
            solicitud,
            domiciliario_id
        )

        domiciliario = obtener_domiciliario(
            db,
            domiciliario
        )

        solicitud.estado = EstadoSolicitud.FINALIZADA

        domiciliario.disponible = True

        db.commit()
        db.refresh(solicitud)

        return solicitud
    