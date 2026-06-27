from fastapi import HTTPException

from utils.rol import RolUsuario
from utils.estados import (
    EstadoSolicitud,
    EstadoOferta
)


# Cliente
def validar_cliente(usuario):

    if usuario.rol != RolUsuario.CLIENTE:

        raise HTTPException(
            status_code=403,
            detail="Solo un cliente puede realizar esta acción."
        )
    
# Domiciliario
def validar_domiciliario(usuario):

    if usuario.rol != RolUsuario.DOMICILIARIO:

        raise HTTPException(
            status_code=403,
            detail="Solo un domiciliario puede realizar esta acción."
        )

def validar_domiciliario_asignado(solicitud, domiciliario_id):
    if solicitud.domiciliario_id != domiciliario_id:
        raise HTTPException(
            status_code=403,
            detail="No tiene permiso para iniciar este servicio."
        )

def validar_domiciliario_disponible(domiciliario):

    if not domiciliario.disponible:
        raise HTTPException(
            status_code=400,
            detail="El domiciliario no está disponible."
        )    

# Solicitud
def validar_solicitud_abierta(solicitud):

    if solicitud.estado != EstadoSolicitud.ABIERTA:

        raise HTTPException(
            status_code=400,
            detail="La solicitud no está abierta."
        )

def validar_solicitud_aceptada(solicitud):

    if solicitud.estado != EstadoSolicitud.ACEPTADA:

        raise HTTPException(
            status_code=400,
            detail="La solicitud no está aceptada."
        )

# Oferta    
def validar_oferta_pendiente(oferta):

    if oferta.estado != EstadoOferta.PENDIENTE:

        raise HTTPException(
            status_code=400,
            detail="La oferta ya fue procesada."
        )