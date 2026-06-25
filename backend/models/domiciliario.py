from sqlalchemy import ( Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
    DateTime
)
from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

from database.base import Base


class Domiciliario(Base):

    __tablename__ = "domiciliarios"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False,
        unique=True
    )

    vehiculo = Column(
        String(50),
        nullable=False
    )

    placa = Column(
        String(20),
        nullable=True
    )

    disponible = Column(
        Boolean,
        default=True
    )

    calificacion_promedio = Column(
        Float,
        default=0
    )

    cantidad_servicios = Column(
        Integer,
        default=0
    )

    usuario = relationship(
        "Usuario"
    )