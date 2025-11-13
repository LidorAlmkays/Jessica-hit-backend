import uvicorn
from fastapi import Depends, FastAPI

from api.http1_1.controllers import health, users
from application.adapters.user_service import UserService
from config import GatewaySettings


class Http1Server:
    """HTTP/1.1 server wrapper that owns the FastAPI application and runtime."""

    def __init__(
        self,
        *,
        settings: GatewaySettings,
        user_service: UserService,
    ) -> None:
        self._settings = settings
        self._user_service = user_service
        self._app: FastAPI | None = None

    @property
    def app(self) -> FastAPI:
        if self._app is None:
            app = FastAPI(
                title=self._settings.service_name,
                version=self._settings.service_version,
            )
            self._register_controllers(app)
            self._app = app
        return self._app

    def serve(self) -> None:
        """Start the ASGI server with the configured FastAPI application."""
        host = self._settings.host
        port = self._settings.port
        log_level = self._settings.log_level
        print(f"Starting HTTP/1.1 server on {host}:{port}")
        uvicorn.run(self.app, host=host, port=port, log_level=log_level)

    def _register_controllers(self, app: FastAPI) -> None:
        """Attach all HTTP controllers to the FastAPI app."""
        def get_user_service() -> UserService:
            return self._user_service

        app.dependency_overrides[UserService] = get_user_service

        app.include_router(health.router)
        app.include_router(users.router)

