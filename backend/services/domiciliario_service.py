from models.domiciliario import Domiciliario

from utils.validaciones import obtener_usuario, validar_perfil_domiciliario
from utils.permisos import validar_domiciliario
from services.solicitud_service import SolicitudService
class DomiciliarioService:

    @staticmethod
    def crear_domiciliario(
        db,
        datos
    ):
        usuario = obtener_usuario(
            db,
            datos.usuario_id
        )

        validar_domiciliario(usuario)

        validar_perfil_domiciliario(
            db,
            datos.usuario_id)

        domiciliario = Domiciliario(
            usuario_id=datos.usuario_id,
            vehiculo=datos.vehiculo,
            placa=datos.placa
        )

        db.add(domiciliario)

        db.commit()

        db.refresh(domiciliario)

        return domiciliario
    
