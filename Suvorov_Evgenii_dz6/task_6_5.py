from sys import argv


def get_users_hobby(name_users_file, name_hobby_file, name_output_file):
    with open(name_users_file, 'r', encoding='utf-8') as f:
        users_list = []
        for line in f:
            line = line.replace('\n', '')
            users_list.append(line)

    with open(name_hobby_file, 'r', encoding='utf-8') as f:
        hobby_list = []
        for line in f:
            line = line.replace('\n', '')
            hobby_list.append(line)

    if len(users_list) >= len(hobby_list):
        result = list(f'{name}: {hobby}\n' for name, hobby in
                      zip(users_list, hobby_list +
                          [None for n in range(len(users_list) - len(hobby_list))]))
        with open(name_output_file, 'w', encoding='utf-8') as f:
            f.writelines(result)
    else:
        raise SystemExit(1)


if __name__ == '__main__':
    get_users_hobby(argv[1], argv[2], argv[3])
