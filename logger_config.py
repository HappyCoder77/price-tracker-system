import logging
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = logging.DEBUG if DEBUG_MODE else logging.INFO


def setup_logging():
    """Configures the global logging settings for the application."""
    logging.basicConfig(
        level=LOG_LEVEL,
        format="%(asctime)s - %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
