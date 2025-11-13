"""Reusable middleware-style dependencies for the HTTP/1.1 API."""

from .json_validation import require_valid_json_for

__all__ = ["require_valid_json_for"]

