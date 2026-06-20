from pydantic import BaseModel, EmailStr


class DomiciliarioCreate(BaseModel):
    nombre: str
    telefono: str
    correo: EmailStr
    password: str
    vehiculo: str

