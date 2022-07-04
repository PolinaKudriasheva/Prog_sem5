"""
    ИСР 2.1. 
    Разработать функцию, возвращающую элементы ряда Фибоначчи по данному максимальному значению.
"""


def fib(n):
  res_lst = [0, 1]
  if n > 1:
    while True:
      cur_num = sum(res_lst[len(res_lst) - 2::])
      if cur_num <= n:
        res_lst.append(cur_num)
      else:
        break
  return res_lst

n = int(input('Введите максимальное значение: '))
print('\nРяд Фибоначчи: ', fib(n))
