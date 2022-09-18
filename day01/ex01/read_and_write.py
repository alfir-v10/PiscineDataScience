def read_and_write(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            new_line = [k for k in line.split("\"") if k not in ['', ',']]
            new_line[3] = new_line[3].strip(',').replace(",", '\t')
            new_line[0] = "\"" + new_line[0].strip() + "\""
            new_line[1] = "\"" + new_line[1].strip() + "\""
            new_line[2] = "\"" + new_line[2].strip() + "\""
            new_line[-2] = "\"" + new_line[-2].strip() + "\""
            lines[i] = "\t".join(new_line).rstrip("\t\n") + "\n"

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)


if __name__ == '__main__':
    read_and_write(path='ds.csv')
