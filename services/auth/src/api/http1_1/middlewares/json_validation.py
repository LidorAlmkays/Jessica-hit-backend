from json import JSONDecodeError
from typing import Type

from fastapi import HTTPException
from pydantic import BaseModel, ValidationError
from starlette.requests import Request


def require_valid_json_for(dto: Type[BaseModel]):
    async def validator(request: Request) -> None:
        if request.method not in {"POST", "PUT", "PATCH"}:
            return

        content_type = request.headers.get("content-type", "")
        if not content_type.startswith("application/json"):
            raise HTTPException(status_code=415, detail="Content-Type must be application/json")

        try:
            payload = await request.json()
        except JSONDecodeError as exc:
            raise HTTPException(status_code=400, detail="Invalid JSON payload supplied.") from exc

        try:
            dto.model_validate(payload)
        except ValidationError as exc:
            raise HTTPException(status_code=422, detail=exc.errors()) from exc

    return validator

