my_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for item in my_lst:
    if 48 <= ord(item[0]) <= 57:
        print(f'"{int(item):02d}"', end=' ')
    elif item[0] == '+':
        print(f'"{item[0]}{int(item):02d}"', end=' ')
    elif item[0] == '-':
        print(f'"{int(item):03d}"', end=' ')
    else:
        print(item, end=' ')
