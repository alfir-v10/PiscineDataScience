#!/usr/bin/env python
import os


def venv_print():
    for k, v in os.environ.items():
        print(k, v)
    print(f"Your current virtual env is {os.environ['VIRTUAL_ENV']}")


if __name__ == '__main__':
    venv_print()

