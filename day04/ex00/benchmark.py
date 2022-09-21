import timeit


def get_email():
    return ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"]


def loop_approach(emails=get_email()):
    new_list = []
    for email in emails:
        if email.find('@gmail.com') != -1:
            new_list.append(email)


def list_comprehension(emails=get_email()):
    new_list = [email for email in emails if email.find('@gmail.com') != -1]


def benchmark():
    n = 900000000
    time_first = timeit.timeit('loop_approach()', 'from __main__ import loop_approach', number=n)
    time_second = timeit.timeit('list_comprehension()', 'from __main__ import list_comprehension', number=n)

    if time_first > time_second:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')
    print(time_first, 'vs', time_second)


if __name__ == "__main__":
    benchmark()
