import pytest

from utils.permisos import *
from utils.estados import EstadoSolicitud, EstadoOferta
from fastapi import HTTPException

class UsuarioFake:
    def __init__(self, rol):
        self.rol = rol
        

def test_validar_domiciliario_correcto():

    usuario = UsuarioFake("DOMICILIARIO")

    validar_domiciliario(usuario)

def test_validar_domiciliario_incorrecto():

    usuario = UsuarioFake("CLIENTE")

    with pytest.raises(HTTPException) as exc:

        validar_domiciliario(usuario)

    assert exc.value.status_code == 403
    assert exc.value.detail == "Solo un domiciliario puede realizar esta acción."


class DomiciliarioFake:
    def __init__(self, disponible =True):
        self.disponible = disponible

class SolicitudFake:
    def __init__(self, estado, domiciliario_id = None):
        self.estado = estado
        self.domiciliario_id = domiciliario_id


class OfertaFake:
    def __init__(self, estado):
        self.estado = estado

# Validar cliente

def test_validar_cliente_correcto():

    usuario = UsuarioFake("CLIENTE")

    validar_cliente(usuario)


def test_validar_cliente_incorrecto():

    usuario = UsuarioFake("DOMICILIARIO")

    with pytest.raises(HTTPException) as exc:

        validar_cliente(usuario)

    assert exc.value.status_code == 403
    assert exc.value.detail == "Solo un cliente puede realizar esta acción."

#  validar_domiciliario_disponible()

def test_domiciliario_disponible():

    domicilio = DomiciliarioFake(True)
    validar_domiciliario_disponible(domicilio)

def test_domiciliario_no_disponible():

    domiciliario = DomiciliarioFake(False)
    
    with pytest.raises(HTTPException) as exc:
        validar_domiciliario_disponible(domiciliario)
        assert exc.value.status_code == 403
        assert exc.value.detail == "El domiciliario no está disponible."

# validar_domiciliario_asignado
def test_domiciliario_asignado():

    solicitud = SolicitudFake(
        EstadoSolicitud.EN_CURSO,
        domiciliario_id=5
    )

    validar_domiciliario_asignado(
        solicitud,
        5
    )


def test_domiciliario_no_asignado():

    solicitud = SolicitudFake(
        EstadoSolicitud.EN_CURSO,
        domiciliario_id=5
    )

    with pytest.raises(HTTPException) as exc:

        validar_domiciliario_asignado(
            solicitud,
            10
        )

    assert exc.value.status_code == 403
    assert exc.value.detail == "No tiene permiso para iniciar este servicio."

# validar_solicitud_abierta()

def test_solicitud_abierta():

    solicitud = SolicitudFake(
        EstadoSolicitud.ABIERTA
    )

    validar_solicitud_abierta(solicitud)

def test_solicitud_no_abierta():

    solicitud = SolicitudFake(
        EstadoSolicitud.CANCELADA
    )

    with pytest.raises(HTTPException) as exc:

        validar_solicitud_abierta(solicitud)

    assert exc.value.status_code == 400
    assert exc.value.detail == "La solicitud no está abierta."

# validar_solicitud_aceptada()

def test_solicitud_aceptada():

    solicitud = SolicitudFake(
        EstadoSolicitud.ACEPTADA
    )

    validar_solicitud_aceptada(solicitud)


def test_solicitud_no_aceptada():

    solicitud = SolicitudFake(
        EstadoSolicitud.ABIERTA
    )

    with pytest.raises(HTTPException) as exc:

        validar_solicitud_aceptada(solicitud)

    assert exc.value.status_code == 400
    assert exc.value.detail == "La solicitud no está aceptada."


# validar_solicitud_en_curso
def test_solicitud_en_curso():

    solicitud = SolicitudFake(
        EstadoSolicitud.EN_CURSO
    )

    validar_solicitud_en_curso(solicitud)


def test_solicitud_no_en_curso():

    solicitud = SolicitudFake(
        EstadoSolicitud.ACEPTADA
    )

    with pytest.raises(HTTPException) as exc:

        validar_solicitud_en_curso(solicitud)

    assert exc.value.status_code == 400
    assert exc.value.detail == "La solicitud no está en curso."

# validar_oferta_pendiente()
def test_oferta_pendiente():

    oferta = OfertaFake(
        EstadoOferta.PENDIENTE
    )

    validar_oferta_pendiente(oferta)


def test_oferta_no_pendiente():

    oferta = OfertaFake(
        EstadoOferta.ACEPTADA
    )

    with pytest.raises(HTTPException) as exc:

        validar_oferta_pendiente(oferta)

    assert exc.value.status_code == 400
    assert exc.value.detail == "La oferta ya fue procesada."