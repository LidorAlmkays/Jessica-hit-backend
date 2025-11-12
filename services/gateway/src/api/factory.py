"""
API factory module.

Use this module to compose transport adapters (HTTP, WebSocket, etc.) once their implementations exist.
"""

from typing import Protocol


class RouterFactory(Protocol):
    """Defines contract for creating transport-specific routers."""

    def build(self) -> object:  # pragma: no cover - placeholder signature
        """Construct and return router instance."""
        raise NotImplementedError


def create_http_api() -> RouterFactory | None:
    """
    Placeholder HTTP API factory.

    Replace return value with actual router factory implementation.
    """
    return None

