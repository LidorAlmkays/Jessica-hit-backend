from collections.abc import Mapping
from typing import Any, Protocol

from api.http1_1.server import Http1Server
from application.adapters.user_service import UserService
from config import GatewaySettings


class ApiFactory:
    """Factory responsible for composing available transport adapters."""

    def __init__(self, *, settings: GatewaySettings) -> None:
        self._settings = settings

    def create_http_server(self, *, user_service: UserService) -> Http1Server:
        return Http1Server(settings=self._settings, user_service=user_service)

