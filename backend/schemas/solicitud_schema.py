from pydantic import BaseModel

class SolicitudCreate(BaseModel):
    cliente_id: int
    origen: str
    destino: str
    descripcion: str | None = None

class SolicitudResponse(BaseModel):
    id: int
    cliente_id: int
    estado: str

    class Config:
        from_attributes = True