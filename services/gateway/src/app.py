def main() -> None:
    """
    Entry point for launching the gateway service.

    Server configuration (host, port, reload, etc.) will be supplied in future revisions.
    """
    from server import GatewayService

    service = GatewayService()
    service.start()

if __name__ == "__main__":
    main()

