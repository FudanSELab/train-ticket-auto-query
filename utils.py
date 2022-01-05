import random
from typing import List
import string


def random_boolean() -> bool:
    return random.choice([True, False])


def random_from_list(l: List):
    return random.choice(l)


def random_from_weighted(d: dict):
    """
    :param d: 带相对权重的字典，eg. {'a': 100, 'b': 50}
    :return: 返回随机选择的key
    """
    total = sum(d.values())    # 权重求和
    ra = random.uniform(0, total)   # 在0与权重和之前获取一个随机数
    curr_sum = 0
    ret = None

    keys = d.keys()
    for k in keys:
        curr_sum += d[k]             # 在遍历中，累加当前权重值
        if ra <= curr_sum:          # 当随机数<=当前权重和时，返回权重key
            ret = k
            break

    return ret


def random_str():
    ''.join(random.choices(string.ascii_letters, k=random.randint(4, 10)))


def random_phone():
    ''.join(random.choices(string.digits, k=random.randint(8, 15)))
