import sys
import timeit
from functools import reduce


def loop_approach():
    s = 0
    for i in range(1, int(sys.argv[3]) + 1):
        s += i * i
    return s


def reduce_approach():
    return reduce(lambda x, y: x + y * y, range(1, int(sys.argv[3]) + 1))


def benchmark():
    options = {
        'loop': 'loop_approach',
        'reduce': 'reduce_approach'
    }

    if len(sys.argv) == 4 and sys.argv[1] in options and sys.argv[2].isdigit() and sys.argv[3].isdigit():
        time_it = timeit.timeit(f'{options[sys.argv[1]]}()', f'from __main__ import {options[sys.argv[1]]}',
                                number=int(sys.argv[2]))
        print(time_it)
    else:
        print('invalid arguments')


if __name__ == "__main__":
    benchmark()