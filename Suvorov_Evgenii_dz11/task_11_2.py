class DivZero(Exception):
    def __init__(self):
        self.msg = 'деление на ноль!'

    def __str__(self):
        return self.msg


x = int(input())
y = int(input())
try:
    if y == 0:
        raise DivZero()
except DivZero:
    print(DivZero())

else:
    print(x / y)
