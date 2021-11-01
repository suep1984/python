from sys import argv

lines_count = 0
with open('bakery.csv', 'r', encoding='utf-8') as f:
    for line in f:
        lines_count += 1


def show_sales(start=0, stop=lines_count):
    res = []
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            res.append(line.replace('\n', ''))
        return res[start:stop]


if __name__ == '__main__':
    if len(argv) == 3:
        for elem in show_sales(int(argv[1]) - 1, int(argv[2])):
            print(elem)
    elif len(argv) == 2:
        for elem in show_sales(int(argv[1]) - 1):
            print(elem)
    else:
        for elem in show_sales():
            print(elem)
