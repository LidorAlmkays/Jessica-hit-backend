from fastapi import APIRouter, Depends

from api.http1_1.dto.RegisterUserRequest import RegisterUserRequest
from api.http1_1.middlewares import require_valid_json_for
from application.adapters.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/register",
    summary="Register a new user",
    dependencies=[Depends(require_valid_json_for(RegisterUserRequest))],
)
async def register_user(
    payload: RegisterUserRequest,
    service: UserService = Depends(UserService),
) -> dict[str, str]:
    print(f"[register_user] email={payload.email} password={payload.password}")
    await service.register(email=payload.email, password=payload.password)
    return {"status": "submitted"}

