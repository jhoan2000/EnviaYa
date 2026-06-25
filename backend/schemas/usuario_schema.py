from pydantic import BaseModel, EmailStr
from typing import Optional


class UsuarioCreate(BaseModel):
    nombre: str
    telefono: str
    correo: EmailStr
    password: str
    direccion_principal: Optional[str] = None
    rol: str

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    telefono: str
    correo: str
    direccion_principal: str | None
    activo: bool
    rol: str
    
    class Config:
        from_attributes = True


class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    telefono: str | None = None
    direccion_principal: str | None = None
    rol: str | None = None