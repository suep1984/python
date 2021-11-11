class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{int(self._income["wage"]) + int(self._income["bonus"])}')


a = Position('Людвиг', 'Аристархов', 'Консьерж', '10000', 2000)
a.get_full_name()
a.get_total_income()
