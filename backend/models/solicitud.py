from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from database.base import Base


class Solicitud(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(String(100), nullable=False)

    origen = Column(String(255))
    
    destino = Column(String(255))

    descripción = Column(String(100), unique=True, nullable=False)
   
    estado = Column(Boolean, default=True)

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())