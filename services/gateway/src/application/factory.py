"""
Factory for constructing application-layer services and orchestrators.

Populate `build_application_services` with the mapping of use-case names to concrete handlers once they exist.
"""

from collections.abc import Mapping
from typing import Any

import structlog

logger = structlog.get_logger(__name__)


def build_application_services(*, dependencies: Mapping[str, Any] | None = None) -> Mapping[str, Any]:
    """
    Create and return the application-layer service registry.

    Parameters
    ----------
    dependencies:
        External resources (repositories, gateways, etc.) produced by the infrastructure layer.
    """
    logger.info("gateway.application.factory.build.start")
    services: dict[str, Any] = {}
    logger.info("gateway.application.factory.build.complete", service_count=len(services))
    return services

