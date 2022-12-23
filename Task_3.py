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
        try:
            result = self.numerator / self.denominator
        except ZeroDivisionError:
            print("На ноль делить нельзя!")
        else:
            print(f"Результат операции - {result}")
        finally:
            print("Программа завершена")  


user_1 = ZeroDenominator(5, 0)
user_1.zero_div()
user_2 = ZeroDenominator(5, 2)
user_2.zero_div()
