def calc_length_num(n):
    lenght = 0
    while (n > 0):
        lenght += 1
        n //= 10
    return lenght

def squareSequenceDigit(n):
    x = 1
    while(True):
        lenght = calc_length_num(x**2) # проверяем длину очередного числа
        if (lenght < n): # если его длина меньше n
            n -= lenght # вычитаем из n эту длину
        else: # иначе возвращаем n-ую цифру числа
            for i in range(n): # путём отсечения последней
                x = x ** 2 % 10
                return x
        x += 1

if __name__ == "__main__":
    print(squareSequenceDigit(1))
    print(squareSequenceDigit(2))
    print(squareSequenceDigit(7))
    print(squareSequenceDigit(12))
    print(squareSequenceDigit(17))
    print(squareSequenceDigit(27))
