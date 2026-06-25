from pydantic import BaseModel


class OfertaCreate(BaseModel):

    solicitud_id: int

    domiciliario_id: int

    valor: float

    tiempo_estimado: int


class OfertaResponse(BaseModel):

    id: int

    solicitud_id: int

    domiciliario_id: int

    valor: float

    tiempo_estimado: int

    estado: str

    class Config:
        from_attributes = True