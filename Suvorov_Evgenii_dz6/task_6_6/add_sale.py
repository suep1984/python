from sys import argv


def add_sale(price):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{float(price)}\n')


if __name__ == '__main__':
    add_sale(argv[1])
