import sys


def letter_starter(email):
    with open("employees.tsv", 'r') as f:
        lines = [line.rstrip().split('\t') for line in f.readlines()]
    for line in lines:
        if email == line[2]:
            print(f"Dear {line[0]}, welcome to our team. We are sure that "
                  f"it will be a pleasure to work with you. "
                  f"That's a precondition for the professionals that our company hires.")
            return
    print("No such email")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        letter_starter(sys.argv[1])