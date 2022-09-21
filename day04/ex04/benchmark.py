import timeit
import random
from collections import Counter


def get_numbers():
    return [random.randint(0, 100) for i in range(1000000)]


def dict_from_list():
    numbers = get_numbers()
    dictionary = {}
    for k in set(numbers):
        dictionary[k] = numbers.count(k)
    return dictionary


def most_common_numbers():
    return [k[0] for k in sorted(dict_from_list().items(), key=lambda n: n[1], reverse=True)[:10]]


def dict_from_counter():
    return Counter(get_numbers())


def top_numbers_counter():
    return [k[0] for k in dict_from_counter().most_common()[:10]]


def becnhmark():
    res_from_list = timeit.timeit('dict_from_list()', 'from __main__ import dict_from_list', number=1)
    most_common_from_list = timeit.timeit('most_common_numbers()', 'from __main__ import most_common_numbers', number=1)
    res_from_counter = timeit.timeit('dict_from_counter()', 'from __main__ import dict_from_counter', number=1)
    most_common_from_counter = timeit.timeit('top_numbers_counter()', 'from __main__ import top_numbers_counter', number=1)

    print(f"my function: {res_from_list}\n Counter: {res_from_counter}\n"
          f"my top: {most_common_from_list}\n Counter's top:{most_common_from_counter}")


if __name__ == '__main__':
    becnhmark()