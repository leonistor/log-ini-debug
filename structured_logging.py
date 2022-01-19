import sys
from loguru import logger

logger.info("Hello structured logging!")

logger.remove(0)

user_ip = "127.0.0.1"

logger.add(sys.stderr, format="{time:HH:mm:ss} | {level} | {extra[ip]} | message")
ip_logger = logger.bind(ip=user_ip)

ip_logger.info("Message from loguru's IP logger")
