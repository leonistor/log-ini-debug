import sys
from loguru import logger

logger.remove(0)
logger.add(
    sys.stderr, format="<y>{time:HH:mm:ss}</y> <b>{level}</b> <le>{message}</le>"
)
logger.info("Hello, pusha customizata!")
