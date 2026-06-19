from pydantic import BaseModel

class DomiciliarioCreate(BaseModel):
    nombre: str
    telefono: str
    vehiculo: str
    estado: str