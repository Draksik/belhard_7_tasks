"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""
from random import randint


class RandSequence:
    n: int
    sequence: list

    def __init__(self, n):
        self.n = n
        self.generate(n)

    def generate(self, n=1):
        self.sequence = []
        for _ in range(n):
            self.sequence.append(randint(-n, n))

    def print_seq(self):
        return self.sequence


prob = RandSequence(5)
prob.generate(8)
print(prob.print_seq())
