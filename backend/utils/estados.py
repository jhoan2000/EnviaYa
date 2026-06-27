
class EstadoSolicitud:
    ABIERTA = "ABIERTA"
    OFERTANDO = "OFERTANDO"
    ACEPTADA = "ACEPTADA"
    EN_CURSO = "EN_CURSO"
    FINALIZADA = "FINALIZADA"
    CANCELADA = "CANCELADA"
    EXPIRADA = "EXPIRADA"

class EstadoOferta:
    PENDIENTE = "PENDIENTE"
    ACEPTADA = "ACEPTADA"
    RECHAZADA = "RECHAZADA"
    CANCELADA = "CANCELADA"


class EstadoDomiciliario:

    DISPONIBLE = "disponible"

    EN_SERVICIO = "en_servicio"

    DESCONECTADO = "desconectado"

    SUSPENDIDO = "suspendido"