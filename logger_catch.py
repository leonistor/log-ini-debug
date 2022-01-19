from __future__ import division
from loguru import logger


@logger.catch
def division(a: int, b: int) -> float:
    return a / b


print(division(2, 1))
print(division(2, 0))
