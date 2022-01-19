from loguru import logger

logger.add("logs/normal.log")
logger.add("logs/compressed.log", compression="zip")

for i in range(10):
    logger.info(f"i is: {i}")
