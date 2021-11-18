class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        new_cell = self.cell + other.cell
        return Cell(new_cell)

    def __sub__(self, other):
        new_cell = self.cell - other.cell
        if new_cell > 0:
            return Cell(new_cell)
        else:
            return 'Incorrect result!'

    def __mul__(self, other):
        new_cell = self.cell * other.cell
        return Cell(new_cell)

    def __floordiv__(self, other):
        new_cell = self.cell // other.cell
        return Cell(new_cell)

    def __truediv__(self, other):
        new_cell = round(self.cell / other.cell)
        return Cell(new_cell)

    def __str__(self):
        return f'{self.cell}'

    def make_order(self, cell_count):
        if self.cell % cell_count == 0:
            return (self.cell // cell_count - 1) * f'{"*" * cell_count}\n' + f'{"*" *  cell_count}'
        else:
            return self.cell // cell_count * f'{"*" * cell_count}\n' + f'{"*" * (self.cell % cell_count)}'


a = Cell(18)
b = Cell(7)
c = a + b
print(a + b)
print(a - c)
print(a * b)
print(a // b)
print(c.make_order(5))
print(c.make_order(6))
print(a / b)
