import sys
import os
import psutil


def ordinary(file):
    with open(file, "r") as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError("Invalid arguments")
        for line in ordinary(sys.argv[1]):
            pass
        process = psutil.Process(os.getpid())
        print(f'Peak memory usage = {round(process.memory_info().rss / 1024 ** 3, 3)} GB')
        cpu_times = process.cpu_times()
        print(f'User Mode Time + System Mode Time = {round(cpu_times.user + cpu_times.system, 2)}s')
    except (ValueError, FileNotFoundError) as err:
        print('Exception: ', err)
