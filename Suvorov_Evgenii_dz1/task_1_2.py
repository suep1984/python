numbers = []
for number in range(0, 1000):
    if number % 2:
        numbers.append(number ** 3)

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

print(sum_of_numbers)

new_sum_of_numbers = 0

for number in numbers:
    sum_of_digits = 0
    new_number = number + 17
    num = new_number
    while num:
        digit = num % 10
        sum_of_digits += digit
        num //= 10
    if not sum_of_digits % 7:
        new_sum_of_numbers += new_number

print(new_sum_of_numbers)
