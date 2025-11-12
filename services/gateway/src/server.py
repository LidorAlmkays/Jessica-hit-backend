class GatewayService:
    def __init__(self) -> None:
        from config import load_gateway_settings

        self.settings = load_gateway_settings()
        self.api_factory = ...
        self.application_factory = ...
        self.infrastructure_factory = ...

    def start(self) -> None:
        resolved_host = self.settings.host
        resolved_port = self.settings.port

        print(f"Starting gateway service on {resolved_host}:{resolved_port}")


def serve() -> None:
    """Backward compatible alias for launching the service."""
    service = GatewayService()
    service.start()








