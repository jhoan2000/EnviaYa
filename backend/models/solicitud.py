from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,DateTime
from sqlalchemy.sql import func

from database.base import Base


class SolicitudServicio(Base):

    __tablename__ = "solicitudes"

    id = Column(Integer, primary_key=True)

    cliente_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )

    origen = Column(String(255))

    destino = Column(String(255))

    descripcion = Column(String(500))

    estado = Column(
        String(30),
        default="abierta"
    )

    fecha_creacion = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )