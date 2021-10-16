my_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_lst2 = []
for item in my_lst:
    if '0' <= item[0] <= '9':
        item = str(f'{int(item):02d}')
        my_lst2.append(item)
        my_lst2.insert(my_lst2.index(item), '"')
        my_lst2.insert((my_lst2.index(item) + 1), '"')
    elif item[0] == '+':
        item = str(f'{item[0]}{int(item[1:]):02d}')
        my_lst2.append(item)
        my_lst2.insert(my_lst2.index(item), '"')
        my_lst2.insert((my_lst2.index(item) + 1), '"')
    else:
        my_lst2.append(item)

print(my_lst2)

print(f'{my_lst2[0]} {"".join(my_lst2[1:4])} {my_lst2[4]} '
      f'{"".join(my_lst2[5:8])} {" ".join(my_lst2[8:12])} '
      f'{"".join(my_lst2[12:15])} {my_lst2[15]}')
