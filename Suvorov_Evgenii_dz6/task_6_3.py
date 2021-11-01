with open('users.csv', 'r', encoding='utf-8') as f:
    users_list = []
    for line in f.readlines():
        line = line.replace(',', ' ')  # из текста задания непонятно, есть ли необходимость в этом
        users_list.append(line.replace('\n', ''))

with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby_list = []
    for line in f.readlines():
        hobby_list.append(line.replace('\n', ''))

if len(users_list) >= len(hobby_list):
    result = {k: v for k, v in
              zip(users_list, hobby_list +
                  [None for n in range(len(users_list) - len(hobby_list))])}  # насколько верна такая конструкция
    # добавления None? У PyCharm она вызывает сомнения
    with open('users_hobby.csv', 'w', encoding='utf-8') as f:
        f.write(str(result))
else:
    raise SystemExit(1)
