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


class ZeroDenominator:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def zero_div(self):
        if self.denominator != 0:
            return self.numerator / self.denominator
        else:
            print("На ноль делить нельзя!")
            return " "


user_1 = ZeroDenominator(5, 0)
print(user_1.zero_div())
user_2 = ZeroDenominator(5, 2)
print(user_2.zero_div())
