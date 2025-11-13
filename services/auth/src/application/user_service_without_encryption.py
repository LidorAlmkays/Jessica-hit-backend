from application.adapters.user_service import UserService


class UserServiceWithoutEncryption(UserService):
    """Development stub: logs credentials rather than applying real encryption."""

    async def register(self, *, email: str, password: str) -> None:
        print(f"[UserServiceWithoutEncryption.register] email={email} password={password}")

    async def login(self, *, email: str, password: str) -> None:
        print(f"[UserServiceWithoutEncryption.login] email={email} password={password}")

