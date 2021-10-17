my_lst = [57.8, 46.51, 97, 134.3, 544, 65.3, 87.21, 2122.4,
          123, 56.9, 35222.88, 2.99, 199.99, 999.09]

# A

for price in my_lst:
    print(f'{int(price)} руб {int(price % int(price) * 100):02d} коп', end=', ')

print('\n')

# B

for price in sorted(my_lst):
    print(f'{int(price)} руб {int(price % int(price) * 100):02d} коп', end=', ')

print('\n')

print(my_lst)

print('\n')

# C

my_lst.sort()
my_lst.reverse()
print(my_lst)

# D

for i in range(-4, 1):
    print(f'{int(my_lst[-i])} руб {int(my_lst[-i] % int(my_lst[-i]) * 100):02d} коп', end=', ')
