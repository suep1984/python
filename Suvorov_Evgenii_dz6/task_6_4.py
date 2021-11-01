with open('users.csv', 'r', encoding='utf-8') as f:
    users_list = []
    for line in f:
        users_list.append(line.replace('\n', ''))

with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby_list = []
    for line in f:
        hobby_list.append(line.replace('\n', ''))

if len(users_list) >= len(hobby_list):
    result = list(f'{name}: {hobby}\n' for name, hobby in
                  zip(users_list, hobby_list +
                      [None for n in range(len(users_list) - len(hobby_list))]))
    with open('users_hobby.txt', 'w', encoding='utf-8') as f:
        f.writelines(result)
else:
    raise SystemExit(1)
