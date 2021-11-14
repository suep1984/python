class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            result.append([x + y for x, y in zip(self.matrix[i], other.matrix[i])])
        return Matrix(result)

    def __str__(self):
        result = ''
        for el in self.matrix:
            result += f'|{" ".join(map(str, el))}|\n'
        return result


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(a)
print(a + b)
