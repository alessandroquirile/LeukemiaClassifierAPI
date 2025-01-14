import logging

logging.basicConfig(
    level=logging.INFO,  # (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)
