class IsNumber(Exception):
    def __init__(self):
        self.msg = 'Incorrect data type'

    def __str__(self):
        return self.msg


result = []
while True:
    element = input('Input data: ')
    if element != 'stop':
        try:
            if not element.isdigit():
                raise IsNumber()
        except IsNumber:
            print(IsNumber())
        else:
            result.append(int(element))
    else:
        break

print(result)
