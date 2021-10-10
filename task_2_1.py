numbers = []
for number in range(0, 1000):
    if number % 2:
        numbers.append(number ** 3)

print('Список кубов нечетных чисел от 1 до 1000: \n\n', numbers, '\n')

sum_of_numbers = 0

for number in numbers:
    sum_of_digits = 0
    num = number
    while num:
        digit = num % 10
        sum_of_digits += digit
        num //= 10
    if not sum_of_digits % 7:
        sum_of_numbers += number

print('Сумма элементов списка, сумма цифр которых кратна 7 равна ', sum_of_numbers, '\n')

for index_of_number in range(len(numbers)):
    numbers[index_of_number] += 17

print('Измененный список: \n\n', numbers, '\n')

new_sum_of_numbers = 0

for number in numbers:
    sum_of_digits = 0
    num = number
    while num:
        digit = num % 10
        sum_of_digits += digit
        num //= 10
    if not sum_of_digits % 7:
        new_sum_of_numbers += number

print('Сумма элементов измененного списка, сумма цифр которых кратна 7 равна ', new_sum_of_numbers, '\n')
