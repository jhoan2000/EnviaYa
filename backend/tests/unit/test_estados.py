from utils.estados import *

# Solicitud
def test_estado_solicitud():
    assert EstadoSolicitud.ABIERTA == "ABIERTA"
    assert EstadoSolicitud.ACEPTADA == "ACEPTADA"
    assert EstadoSolicitud.EN_CURSO == "EN_CURSO"
    assert EstadoSolicitud.FINALIZADA == "FINALIZADA"
    assert EstadoSolicitud.CANCELADA == "CANCELADA"

# Oferta
def test_estado_oferta():
    assert EstadoOferta.PENDIENTE == "PENDIENTE"
    assert EstadoOferta.ACEPTADA == "ACEPTADA"
    assert EstadoOferta.RECHAZADA == "RECHAZADA"
    assert EstadoOferta.CANCELADA == "CANCELADA"

# Domiciliario
def test_estado_domiciliario():
    assert EstadoDomiciliario.DISPONIBLE == "DISPONIBLE"
    assert EstadoDomiciliario.EN_SERVICIO == "EN_SERVICIO"
    assert EstadoDomiciliario.DESCONECTADO == "DESCONECTADO"
    assert EstadoDomiciliario.SUSPENDIDO == "SUSPENDIDO"