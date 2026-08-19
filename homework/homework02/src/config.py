"""Configuration helpers for the Stage 02 tooling assignment."""

import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_env() -> bool:
    """Load variables from the homework's local .env file."""
    return load_dotenv(PROJECT_ROOT / ".env")


def get_key(name: str) -> str:
    """Return a required environment variable or raise a clear error."""
    value = os.getenv(name)
    if not value:
        raise KeyError(f"Missing required environment variable: {name}")
    return value
