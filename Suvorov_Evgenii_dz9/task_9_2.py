class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mas_asphalt(self, mas, tin):
        result = self._length * self._width * mas * tin // 1000
        return f'{result} т'


a = Road(20, 5000)
print(a.get_mas_asphalt(25, 1))
