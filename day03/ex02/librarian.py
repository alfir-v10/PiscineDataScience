#!/usr/bin/env python

import os


def install(packages):
    try:
        venv = os.environ['VIRTUAL_ENV']
        user = venv.split('\\')[-1]
        print(user)
        print(venv)
        if venv.endswith(f'{user}'):
            packages_string = " ".join(packages)
            os.system(f"pip install {packages_string}")
            os.system("pip freeze > requirements.txt -l")
            os.system(f"tar cvf {user}.tar {venv}")
        else:
            raise ValueError("wrong environment variable")
    except KeyError as e:
        print(e)


if __name__ == '__main__':
    install(["beautifulsoup4", "PyTest", "requests"])