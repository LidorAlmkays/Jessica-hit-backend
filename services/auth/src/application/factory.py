from application.adapters.user_service import UserService
from application.user_service_without_encryption import UserServiceWithoutEncryption
from services.gateway.src.config import GatewaySettings


class ApplicationFactory:
    def __init__(self,*,settings: GatewaySettings) -> None:
        self._settings = settings
    def get_user_service() -> UserService:
        """Create the default user service implementation."""
        return UserServiceWithoutEncryption()

