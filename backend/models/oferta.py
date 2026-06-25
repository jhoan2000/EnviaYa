from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey,DateTime
from sqlalchemy.sql import func

from database.base import Base

from utils.estados import EstadoOferta


class Oferta(Base):

    __tablename__ = "ofertas"

    id = Column(Integer, primary_key=True)

    solicitud_id = Column(
        Integer,
        ForeignKey("solicitudes.id"),
        nullable=False
    )

    domiciliario_id = Column(
        Integer,
        ForeignKey("domiciliarios.id"),
        nullable=False
    )

    valor = Column(
        Float,
        nullable=False
    )

    tiempo_estimado = Column(
        Integer,
        nullable=False
    )

    estado = Column(
        String(20),
        default=EstadoOferta.PENDIENTE
    )

    fecha_creacion = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )