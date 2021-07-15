import random
from typing import List
import string


def random_boolean() -> bool:
    return random.choice([True, False])


def random_form_list(l: List):
    return random.choice(l)


def random_str():
    ''.join(random.choices(string.ascii_letters, k=random.randint(4, 10)))


def random_phone():
    ''.join(random.choices(string.digits, k=random.randint(8, 15)))
