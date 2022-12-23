"""
Задание 3.

Создайте собственный класс-исключение,
обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных,
вводимых пользователем. При вводе
пользователем нуля в качестве делителя
программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""

class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_error():
    try:
        x = int(input('Введите делимое: '))
        y = int(input('Введите делитель: '))
        if y == 0:
            raise ZeroDiv("На ноль делить нельзя!")
        else:
            res = x / y
            return res
    except ValueError:
        return "Вы ввели не число"
    except ZeroDiv as err:
        return err


print(my_error())
