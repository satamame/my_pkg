import numpy as np

from .character import Character


def generate_extras(min_age, max_age, count):
    ages = np.random.randint(min_age, max_age + 1, count)
    for age in ages:
        yield Character(age=age)
