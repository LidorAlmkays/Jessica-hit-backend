from app import App


def main() -> None:
    """
    Entry point for launching the gateway service.

    Server configuration (host, port, reload, etc.) will be supplied in future revisions.
    """
    service = App()
    service.start()


if __name__ == "__main__":
    main()
