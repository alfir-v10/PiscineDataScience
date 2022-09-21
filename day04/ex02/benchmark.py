import timeit
import sys


def get_email():
    return ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"]


def loop_approach(emails=get_email()):
    new_list = []
    for email in emails:
        if email.find('@gmail.com') != -1:
            new_list.append(email)


def list_comprehension(emails=get_email()):
    new_list = [email for email in emails if email.find('@gmail.com') != -1]


def map_approach(emails=get_email()):
    new_list = map(lambda email: email if email.find('@gmail.com') != -1 else None, emails)


def filter_approach(emails=get_email()):
    new_list = filter(lambda email: email if email.find('@gmail.com') != -1 else None, emails)


def benchmark():
    n = 900000000

    options = {
        'list_comprehension': 'list_comprehension',
        'loop': 'loop_approach',
        'map': 'map_approach',
        'filter': 'filter_approach'
    }

    if len(sys.argv) == 3 and sys.argv[1] in options and sys.argv[2].isdigit():
        time_it = timeit.timeit(f'{options[sys.argv[1]]}()', f'from __main__ import {options[sys.argv[1]]}',
                                number=int(sys.argv[2]))
        print(time_it)
    else:
        print('invalid arguments')


if __name__ == "__main__":
    benchmark()
