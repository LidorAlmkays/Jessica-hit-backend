"""
Factory for provisioning infrastructure adapters (databases, message brokers, external services).
"""

from collections.abc import Mapping
from typing import Any

import structlog

logger = structlog.get_logger(__name__)


def build_infrastructure(*, settings: Mapping[str, Any] | None = None) -> Mapping[str, Any]:
    """
    Create infrastructure adapters and return them as a dependency mapping.

    Parameters
    ----------
    settings:
        Connection details, credentials, or feature toggles required by adapters.
    """
    logger.info("gateway.infrastructure.factory.build.start")
    dependencies: dict[str, Any] = {}
    logger.info("gateway.infrastructure.factory.build.complete", dependency_count=len(dependencies))
    return dependencies

