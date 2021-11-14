from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def calculation_expense(self):
        pass


class Coat(Wear):
    def __init__(self, v):
        self.v = v

    @property
    def calculation_expense(self):
        return self.v / 6.5 + 0.5


class Costume(Wear):
    def __init__(self, h):
        self.h = h

    @property
    def calculation_expense(self):
        return self.h * 2 + 0.3


a = Coat(52)
b = Costume(180)
print(a.calculation_expense)
print(a.calculation_expense + b.calculation_expense)
