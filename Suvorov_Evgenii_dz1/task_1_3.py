for item in range(1, 101):
    if item % 10 == 1 and (item // 10 == 0 or item // 10 >= 2):
        print(f'{item} процент')
    elif 2 <= item % 10 <= 4 and (item // 10 == 0 or item // 10 >= 2):
        print(f'{item} процента')
    elif item // 10 == 1 or item % 10 == 0 or 5 <= item % 10 <= 9:
        print(f'{item} процентов')
