from fastapi import HTTPException

from models.usuario import Usuario
from models.domiciliario import Domiciliario
from models.solicitud import Solicitud
from models.oferta import Oferta

# Usuarios

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

# Domiciliarios
def obtener_domiciliario(db, domiciliario_id: int):
    domiciliario = (
        db.query(Domiciliario)
        .filter(Domiciliario.id == domiciliario_id)
        .first()
    )

    if not domiciliario:
        raise HTTPException(
            status_code=404,
            detail="Domiciliario no encontrado"
        )

    return domiciliario

def validar_perfil_domiciliario(db, usuario_id: int):

    domiciliario = (
        db.query(Domiciliario)
        .filter(
            Domiciliario.usuario_id == usuario_id
        )
        .first()
    )

    if domiciliario:

        raise HTTPException(
            status_code=400,
            detail="El usuario ya tiene perfil de domiciliario."
        )

# Solicitudes
def obtener_solicitud(db, solicitud_id: int):

    solicitud = (
        db.query(Solicitud)
        .filter(Solicitud.id == solicitud_id)
        .first()
    )

    if not solicitud:
        raise HTTPException(
            status_code=404,
            detail="Solicitud no encontrada"
        )

    return solicitud

# Ofertas
def obtener_oferta(db, oferta_id: int):

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

    return oferta


