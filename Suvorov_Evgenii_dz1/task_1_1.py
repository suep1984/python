duration = int(input('Введите кол-во секунд: '))
SECOND_IN_MINUT = 60
SECOND_IN_HOUR = 3600
SECOND_IN_DAY = 86400
HOUR_IN_DAY = 24
seconds = duration % SECOND_IN_MINUT
minuts = duration // SECOND_IN_MINUT % SECOND_IN_MINUT
hours = duration // SECOND_IN_HOUR % HOUR_IN_DAY
days = duration // SECOND_IN_DAY
if duration < 60:
    print(seconds, 'сек')
elif 60 <= duration < 3600:
    print(f'{minuts} мин {seconds} сек')
elif 3600 <= duration < 86400:
    print(f'{hours} час {minuts} мин {seconds} сек')
elif duration >= 86400:
    print(f'{days} дн {hours} час {minuts} мин {seconds} сек')
