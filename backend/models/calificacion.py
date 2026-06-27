from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
    DateTime,
    Boolean
)

from sqlalchemy.sql import func

from database.base import Base


class Calificacion(Base):

    __tablename__ = "calificaciones"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    solicitud_id = Column(
        Integer,
        ForeignKey("solicitudes.id"),
        nullable=False,
        unique=True
    )

    calificacion_cliente = Column(
        Integer,
        nullable=True
    )

    comentario_cliente = Column(
        Text,
        nullable=True
    )

    calificacion_domiciliario = Column(
        Integer,
        nullable=True
    )

    comentario_domiciliario = Column(
        Text,
        nullable=True
    )
    calificacion_pendiente = Column(
        Boolean,
        default=True,
        nullable=False
        )

    fecha = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )