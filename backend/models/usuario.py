from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

from database.base import Base

from utils.rol import RolUsuario

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String(100), nullable=False)

    telefono = Column(String(20), nullable=False)

    correo = Column(String(100), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    direccion_principal = Column(String(255))

    activo = Column(Boolean, default=True)

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    rol = Column(String(20), nullable=False, default=RolUsuario.CLIENTE)
    """ perfil_domiciliario = relationship(
    "Domiciliario",
    uselist=False
    ) """
    