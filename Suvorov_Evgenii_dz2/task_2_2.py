my_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for item in my_lst:
    try:
        if type(int(item)) == int:
            item_int = int(item)
            item_str = str(item)
            if item_str[0] == chr(43) and 0 <= item_int < 10:
                item_str = f'"{item_str[0]}0{item_int}"'
                print(item_str, end=' ')
            elif item_str[0] == chr(43) and item_int >= 10:
                item_str = f'"{item_str[0]}{item_int}"'
                print(item_str, end=' ')
                # my_lst2.append(item_str)
                # my_lst2.insert(my_lst2.index(item_str), '"')
                # my_lst2.insert((my_lst2.index(item_str) + 1), '"')
            elif 0 <= item_int < 10:
                item_int = f'"0{item_int}"'
                print(item_int, end=' ')
                # my_lst2.append(item_int)
                # my_lst2.insert(my_lst2.index(item_int), '"')
                # my_lst2.insert((my_lst2.index(item_int) + 1), '"')
            else:
                item_int = f'"{item_int}"'
                print(item_int, end=' ')
                # my_lst2.append(item_int)
                # my_lst2.insert(my_lst2.index(item_int), '"')
                # my_lst2.insert((my_lst2.index(item_int) + 1), '"')
    except ValueError:
        print(item, end=' ')
        # my_lst2.append(item)
