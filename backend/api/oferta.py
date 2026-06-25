from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencias import get_db

from schemas.oferta_schema import (
    OfertaCreate,
    OfertaResponse
)

from services.oferta_service import (
    OfertaService
)

router = APIRouter(
    prefix="/ofertas",
    tags=["Ofertas"]
)


@router.post(
    "/",
    response_model=OfertaResponse
)
def crear_oferta(
    datos: OfertaCreate,
    db: Session = Depends(get_db)
):

    return OfertaService.crear_oferta(
        db,
        datos
    )