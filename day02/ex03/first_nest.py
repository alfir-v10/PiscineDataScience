import sys


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        try:
            with open(self.path, 'r') as f:
                all_lines = [line.rstrip('\n').split(',') for line in f.readlines()]
                header = all_lines[0]
                lines = all_lines[1:]
            for i, line in enumerate(lines):
                if len(line) != 2 or (i > 0 and ('0' not in line or '1' not in line)):
                    raise ValueError('file with a different structure was given')
            if has_header:
                return [[int(line[0]), int(line[1])] for line in lines]
            return [[int(line[0]), int(line[1])] for line in lines]
        except (OSError, ValueError) as e:
            print('Exception: ', e)

    class Calculations:

        @classmethod
        def counts(cls, lines):
            heads = 0
            tails = 0
            for i in lines:
                if i[0] == 1:
                    heads += 1
                else:
                    tails += 1
            return heads, tails

        @classmethod
        def fractions(cls, head, tails):
            return head / (head + tails) * 100, tails / (head + tails) * 100


if __name__ == '__main__':
    if len(sys.argv) == 2:
        lines = Research(sys.argv[1]).file_reader()
        if lines:
            print(lines)
            counts = Research.Calculations.counts(lines)
            print(*counts)
            print(*Research.Calculations.fractions(*counts))
