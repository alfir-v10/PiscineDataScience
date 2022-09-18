def data_types():
    data = [int, str, float, bool, list, dict, tuple, set]
    data_types = [type(d()).__name__ for d in data]
    print(data_types)


if __name__ == '__main__':
    data_types()