from fastapi import APIRouter

from api.http1_1.dto.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse, summary="Gateway health probe")
async def get_health() -> HealthResponse:
    return HealthResponse(status="ok")

