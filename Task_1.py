"""Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора
класса (метод init()),
который должен принимать данные
(список списков) для формирования
матрицы.
[[], [], []]
Следующий шаг — реализовать
перегрузку метода str() для вывода
матрицы в привычном виде.
Далее реализовать перегрузку метода
add() для реализации операции
сложения двух объектов класса Matrix
(двух матриц).
Результатом сложения должна быть
новая матрица.

Подсказка: сложение элементов матриц
 выполнять поэлементно —
первый элемент первой строки первой
матрицы складываем
с первым элементом первой строки
второй матрицы и т.д."""


class Matrix:
    
    def __init__(self, list_1):
        self.list_1 = list_1

    def __str__(self):
        return str('\n'.join(' '.join(str(el) for el in i) for i in self.list_1))
    def __add__(self, other):
        try:    
            result = []
            numbers = []
            for i in range(len(self.list_1)):
                for j in range(len(self.list_1[0])):
                    summa = other.list_1[i][j] + self.list_1[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.list_1):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        except IndexError:
            return "Размеры матриц не совпадают. Операция невозможна!"

m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m3 = Matrix([[1, 2, 3], [4, 5, 6]])
print(m1 + m2)
print(m1 + m3)


  
m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m1 + m2)
