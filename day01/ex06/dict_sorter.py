def to_dictionary():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    new_dict = {}
    for value in list_of_tuples:
        if value[1] not in new_dict:
            new_dict[value[1]] = []
            new_dict[value[1]].append(value[0])
        else:
            new_dict[value[1]].append(value[0])

    for k, v in new_dict.items():
        new_dict[k] = sorted(v)

    for key in sorted([int(k) for k in list(new_dict)], reverse=True):
        for val in new_dict[str(key)]:
             print(val)


if __name__ == "__main__":
        to_dictionary()