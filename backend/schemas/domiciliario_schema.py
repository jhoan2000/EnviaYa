from pydantic import BaseModel, EmailStr

from pydantic import BaseModel


class DomiciliarioCreate(BaseModel):

    usuario_id: int

    vehiculo: str

    placa: str | None = None


class DomiciliarioResponse(BaseModel):

    id: int

    usuario_id: int

    vehiculo: str

    placa: str | None

    disponible: bool

    calificacion_promedio: float

    cantidad_servicios: int

    class Config:
        from_attributes = True