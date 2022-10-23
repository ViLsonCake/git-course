from random import randint

def random_number(x: int, y: int) -> int:
    return randint(x, y) if x <= y else randint(y, x)