from fastapi import APIRouter
from models.domiciliario import DomiciliarioCreate
from services.domiciliario_service import crear_domiciliario

router = APIRouter(prefix="/domiciliarios", tags=["Domiciliarios"])

@router.post("")
def crear(domiciliario: DomiciliarioCreate):
    return {
        "mensaje": "Domiciliario creado",
        "data": crear_domiciliario(domiciliario)
    }