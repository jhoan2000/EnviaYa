from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,DateTime
from sqlalchemy.sql import func

from database.base import Base

class Solicitud(Base):

    __tablename__ = "solicitudes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    cliente_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )

    origen = Column(
        String(255),
        nullable=False
    )

    destino = Column(
        String(255),
        nullable=False
    )

    descripcion = Column(
        String(500)
    )

    estado = Column(
        String(20),
        default="ABIERTA"
    )

    fecha_creacion = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    fecha_aceptacion = Column(
        DateTime(timezone=True)
    )

    fecha_inicio = Column(
        DateTime(timezone=True)
    )

    fecha_finalizacion = Column(
        DateTime(timezone=True)
    )

    fecha_cancelacion = Column(
        DateTime(timezone=True)
    )


