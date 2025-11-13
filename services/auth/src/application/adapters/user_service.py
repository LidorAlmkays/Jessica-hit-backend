from __future__ import annotations

from abc import ABC, abstractmethod


class UserService(ABC):
    """Contract describing user-related operations required by the API layer."""

    @abstractmethod
    async def register(self, *, email: str, password: str) -> None:
        """Register a new user with the provided credentials."""

    @abstractmethod
    async def login(self, *, email: str, password: str) -> None:
        """Authenticate a user with the provided credentials."""

