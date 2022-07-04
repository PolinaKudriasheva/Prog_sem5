"""
    ИСР 2.2. 
    Создание программы, возвращающей список чисел Фибоначчи с помощью итератора.
"""


class FibonacchiLst:
    def __init__(self, max):
        self.max = max
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.prev
        if fib > self.max:
            raise StopIteration
        self.prev, self.curr = self.curr, self.prev + self.curr
        return fib


def main():
    n = int(input("Введите максимальное значение: "))
    print('\nРяд Фибоначчи: ', list(FibonacchiLst(n)))


main()
