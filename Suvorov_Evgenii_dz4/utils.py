from requests import get
from decimal import Decimal
from datetime import date


def currency_rates(currency):
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    response = get(url)
    contents = response.text
    index_date = contents.find('Date="')
    date_in_list = contents[index_date + 6:index_date + 16].split('.')
    date_output = date(int(date_in_list[2]), int(date_in_list[1]), int(date_in_list[0]))
    code = []
    value = []
    for s in contents:
        index_code = contents.find('<CharCode>')
        contents = contents[index_code + 10:]
        if contents[0:3].isupper():
            code.append(contents[0:3])
        else:
            break
        index_value = contents.find('<Value>')
        contents = contents[index_value + 7:]
        number = Decimal(contents[0:7].replace(',', '.'))
        value.append(number.quantize(Decimal('1.00')))
    dict_of_currency = {k: v for k, v in zip(code, value)}
    return dict_of_currency.get(currency.upper()), date_output


if __name__ == '__main__':
    example1, example_date = currency_rates('USD')
    example2, example_date = currency_rates('eur')
    print(f'{example1}, {example_date}')
    print(f'{example2}, {example_date}')
