"""Load local configuration for Homework 2."""

import os
from pathlib import Path

from dotenv import load_dotenv


ENV_FILE = Path(__file__).resolve().parents[1] / ".env"


# --- Environment access --- #

def load_env() -> bool:
    """Load values from the Homework 2 .env file."""
    return load_dotenv(dotenv_path=ENV_FILE)


def get_key(name: str, default: str | None = None) -> str | None:
    """Return one configuration value from the environment."""
    return os.getenv(name, default)
