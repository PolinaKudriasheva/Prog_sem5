"""
    ИСР 2.1
    На основе кода, предоставленного преподавателем, реализовать генератор чисел ряда Фибоначчи. Генератор требуется создать двумя вариантами: с помощью генератора списков, с помощью функции, внутри которой yield.
"""

from itertools import islice

class FibonacchiLst:
    def __init__(self, max_value):
        self.max_value = max_value
        self.lst = [0, 1]
    
    def __getitem__(self, idx):
        if self.max_value < 0:
            raise IndexError(idx)
        
        if idx > 0:
            if self.max_value == 0:
                raise IndexError(idx)
                        
            if idx == 1:
                return self.lst[1]
            
            if idx == 2 and self.max_value == 1:
                raise IndexError(idx)
            
            cur_el = self.lst[0] + self.lst[1]
            del self.lst[0]
            self.lst.append(cur_el)
            
            if cur_el > self.max_value:
                raise IndexError(idx)
            
            return self.lst[1]
        
        else:
            return self.lst[0]


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    fib_lst = [num for num in FibonacchiLst(10)]
    print(fib_lst)
    
    fib_lst = list(islice(fib(), 10))
    print(fib_lst)
