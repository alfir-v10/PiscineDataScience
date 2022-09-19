import sys

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        try:
            with open(self.path, 'r') as f:
                lines = [line.rstrip('\n').split(',') for line in f.readlines()]
            for i, line in enumerate(lines):
                if len(line) != 2 or (i > 0 and ('0' not in line or '1' not in line)):
                    raise ValueError('file with a different structure was given')
            return "\n".join([','.join(line) for line in lines])
        except (OSError, ValueError) as e:
            print('Exception: ', e)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        text = Research(sys.argv[1]).file_reader()
        if text:
            print(text)