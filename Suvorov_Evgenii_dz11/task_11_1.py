import time


class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def date_int(cls, date_str):
        day = int(date_str.split('-')[0])
        month = int(date_str.split('-')[1])
        year = int(date_str.split('-')[2])
        if cls.validation_date(date_str):
            return day, month, year

    @staticmethod
    def validation_date(date_str):
        valid_date = time.strptime(date_str, '%d-%m-%Y')
        if valid_date:
            return True
        else:
            print('Invalid date!')


print(Date.date_int('30-11-2009'))
print(Date.date_int('31-11-2009'))
