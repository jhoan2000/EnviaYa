from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencias import get_db

from schemas.domiciliario_schema import (
    DomiciliarioCreate,
    DomiciliarioResponse
)

from services.domiciliario_service import (
    DomiciliarioService
)

router = APIRouter(
    prefix="/domiciliarios",
    tags=["Domiciliarios"]
)


@router.post(
    "/",
    response_model=DomiciliarioResponse
)
def crear_domiciliario(
    datos: DomiciliarioCreate,
    db: Session = Depends(get_db)
):

    return DomiciliarioService.crear_domiciliario(
        db,
        datos
    )