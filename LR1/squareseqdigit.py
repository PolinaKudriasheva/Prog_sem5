def calc_length_num(n):
    lenght = 0
    while (n > 0):
        lenght += 1
        n //= 10
    return lenght

def squareSequenceDigit(n):
    k = n
    x = 1
    while(True):
        lenght = calc_length_num(x**2) 
        if (lenght < n): 
            n -= lenght 
        else: 
            if k % 2 != 0 or k <= 3:
              x = x ** 2 % 10
            else:
              x = x ** 2 // 10
            return x
        x += 1

if __name__ == "__main__":
    print(squareSequenceDigit(1))
    print(squareSequenceDigit(2))
    print(squareSequenceDigit(7))
    print(squareSequenceDigit(12))
    print(squareSequenceDigit(17))
    print(squareSequenceDigit(27))
