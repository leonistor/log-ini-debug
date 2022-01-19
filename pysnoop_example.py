import pysnooper


@pysnooper.snoop()
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]


result = number_to_bits(6)
print(f"result: {result}")

import random


def foo():
    lst = []
    for i in range(10):
        lst.append(random.randrange(1, 100))
    with pysnooper.snoop():
        lower, upper = min(lst), max(lst)
        mid = (lower + upper) / 2
        print(lower, mid, upper)


foo()
