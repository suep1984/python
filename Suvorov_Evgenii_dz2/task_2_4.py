my_lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
          'директор аэлита']

for string in my_lst:
    i = -1
    rev_name = ''
    while string[i] != ' ':
        rev_name += string[i]
        i -= 1
    print(f'Привет, {rev_name[::-1].capitalize()}!')
