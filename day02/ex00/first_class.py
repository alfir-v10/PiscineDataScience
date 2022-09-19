class Must_read:
    with open('data.csv', 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        for line in lines:
            print(line)


if __name__ == "__main__":
    pass