from pydantic import BaseModel, EmailStr

from pydantic import BaseModel

import datetime

class CalificacionCreate(BaseModel):

    solicitud_id: int

    calificacion_cliente: int | None = None
    comentario_cliente: str | None = None

    calificacion_domiciliario: int | None = None
    comentario_domiciliario: str | None = None

class CalificacionResponse(BaseModel):

    id: int

    solicitud_id: int

    calificacion_cliente: int | None
    comentario_cliente: str | None

    calificacion_domiciliario: int | None
    comentario_domiciliario: str | None

    fecha: datetime

    class Config:
        from_attributes = True