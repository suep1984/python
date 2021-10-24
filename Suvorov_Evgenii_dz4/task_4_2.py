from requests import get
from decimal import Decimal


def currency_rates(currency):
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    response = get(url)
    contents = response.text
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
    return dict_of_currency.get(currency.upper())


if __name__ == '__main__':
    a = currency_rates('usd')
    b = currency_rates('EUR')
    print(a, b)
