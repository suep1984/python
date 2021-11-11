class Stationery:
    def __init__(self, title='Запуск отрисовки'):
        self.title = title

    def draw(self):
        print(self.title)


class Pen(Stationery):
    def draw(self):
        print('Пишем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Помечаем маркером')


a = Stationery()
a.draw()
b = Pen('Ручка')
b.draw()
c = Pencil('Карандаш')
c.draw()
d = Handle('Маркер')
d.draw()
