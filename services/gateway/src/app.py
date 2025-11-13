from typing import Protocol

from api import ApiFactory
from api.http1_1.server import Http1Server
from application.factory import ApplicationFactory, get_user_service
from application.adapters.user_service import UserService
from config import GatewaySettings, load_gateway_settings


class App:
    def __init__(self) -> None:
        self.settings = load_gateway_settings()
        self.api_factory = ApiFactory(settings=self.settings)
        self.application_factory = ApplicationFactory(settings=self.settings)
        self.infrastructure_factory = ...

    def start(self) -> Http1Server:
        """Build the HTTP server instance for the gateway."""

        http_server = self.api_factory.create_http_server(user_service=self.application_factory.get_user_service())
        http_server.serve()

