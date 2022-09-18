import sys


def names_extractor(path):
    with open("employees.tsv", "a") as f2, open(path) as f1:
        emails = f1.readlines()
        f2.write("Name\tSurname\tE-mail\n")
        for email in emails:
            name, surname = [k.capitalize() for k in email.split('@')[0].split('.')]
            line = f'{name}\t{surname}\t{email}'
            f2.write(line)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        names_extractor(sys.argv[1])