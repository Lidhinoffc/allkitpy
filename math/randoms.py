import random


def random_int(start, end):
    return random.randint(start, end)


def random_float():
    return random.random()


def choice(values):
    return random.choice(values)


def shuffle(values):
    random.shuffle(values)
    return values