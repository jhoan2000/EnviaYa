from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencias import get_db

from schemas.solicitud_schema import (
    SolicitudCreate,
    SolicitudResponse
)

from services.solicitud_service import (
    SolicitudService
)

router = APIRouter(
    prefix="/solicitudes",
    tags=["Solicitudes"]
)


@router.post(
    "/",
    response_model=SolicitudResponse
)
def crear_solicitud(
    datos: SolicitudCreate,
    db: Session = Depends(get_db)
):

    return SolicitudService.crear_solicitud(
        db,
        datos
    )

@router.put(
    "/{solicitud_id}/iniciar",
    response_model=SolicitudResponse
)
def iniciar_servicio(
    solicitud_id: int,
    db: Session = Depends(get_db)
):
    return SolicitudService.iniciar_servicio(
        db,solicitud_id
    )