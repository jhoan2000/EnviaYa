from utils.estados import *

# Solicitud
def test_estado_solicitud_abierta():
    assert EstadoSolicitud.ABIERTA == "ABIERTA"
def test_estado_solicitud_aceptada():
    assert EstadoSolicitud.ACEPTADA == "ACEPTADA"
def test_estado_solicitud_en_curso():
    assert EstadoSolicitud.EN_CURSO == "EN_CURSO"
def test_estado_solicitud_finalizada():
    assert EstadoSolicitud.FINALIZADA == "FINALIZADA"
def test_estado_solicitud_cancelada():
    assert EstadoSolicitud.CANCELADA == "CANCELADA"

# Oferta
def test_estado_oferta_pendiente():
    assert EstadoOferta.PENDIENTE == "PENDIENTE"
def test_estado_oferta_aceptada():
    assert EstadoOferta.ACEPTADA == "ACEPTADA"
def test_estado_oferta_rechazada():
    assert EstadoOferta.RECHAZADA == "RECHAZADA"
def test_estado_oferta_cancelada():
    assert EstadoOferta.CANCELADA == "CANCELADA"

# Domiciliario
def test_estado_domiciliario_disponible():
    assert EstadoDomiciliario.DISPONIBLE == "DISPONIBLE"
def test_estado_domiciliario_en_servicio():
    assert EstadoDomiciliario.EN_SERVICIO == "EN_SERVICIO"
def test_estado_domiciliario_desconectado():
    assert EstadoDomiciliario.DESCONECTADO == "DESCONECTADO"
def test_estado_domiciliario_suspendido():
    assert EstadoDomiciliario.SUSPENDIDO == "SUSPENDIDO"