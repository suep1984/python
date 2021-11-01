from sys import argv


def replace_sales(idx, replacement):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        tmp = [line for line in f]
        if len(tmp) >= int(idx):
            for item in tmp:
                if tmp.index(item) == int(idx) - 1:
                    tmp[tmp.index(item)] = str(float(replacement)) + '\n'
                else:
                    continue
        else:
            print('Запись не существует')
    with open('bakery.csv', 'w', encoding='utf-8') as f:
        f.writelines(tmp)


if __name__ == '__main__':
    if len(argv) == 3:
        replace_sales(argv[1], argv[2])
    else:
        print('Неверный ввод')
