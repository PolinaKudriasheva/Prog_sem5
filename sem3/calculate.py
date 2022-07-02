from calcprint import print_results, write_log
import unittest

#глобальная переменная-словарь, содержащая параметры, равные по умолчанию None, которые потом будут браться из файла
PARAMS = {'precision': None,
        'output_type': None,
        'possible_types': None,
        'dest': None}


def load_params(file="params.ini"):
    ''' Функция загружает параметры вычислений из внешнего файла, 
    которым по умолчанию является params.ini '''

    # with используется, чтобы избежать предупреждения о незакрытом файле
    global PARAMS
    try: # пробуем открыть файл
        f = open(file, 'r', errors='ignore')
        f.close()
    except FileNotFoundError: # исключение ошибки несуществующего файла
        print("Такого файла с параметрами не существует")
    else:
        with open(file, 'r', errors='ignore') as f:
            lines = f.readlines()
            for l in lines:
                param = l.split('=') #делим каждую строку по символу равно на два элемента списка param
                param[1] = param[1].strip('\n') #убираем перенос строки

                if param[0] != 'dest': #если параметр указывает на путь
                    param[1] = eval(param[1])
                PARAMS[param[0]] = param[1]#значение Params с ключом, совпадающим со словом до равно в файле приравнивается к значеню после равно


def convert_precision(prec):
    # функция, позволяющая преобразовывать значение в целочисленный формат
    ''''
    Преобразует точность данную в виде числа с плавающей точкой в целое число, возможное для использования с функцией round.
    >>> convert_precision(0.001)
    3
    >>> convert_precision(0.000000001)
    9
    >>> convert_precision('string')
    None
    '''    
    #пока точность меньше 1, умножаем на 10, в i записывается кол-во знаков после запятой
    i=0
    while prec<1:
        prec*=10
        i+=1
    return i


# функция ввода с клавиатуры
def user_input():
    args = []

    while True:
        val = input("Enter value: ")
        try:
            if val == "": # если вводится пустая строка, то прекращается считывание аргументов
                break
            val = float(val) 
        except ValueError: # если нельзя перевести во float, то введена строка и возникает исключение
            print("Введите число в правильном формате (разделитель дробной части '.') ") #при этом выводится эта строка
        else:
            args.append(val) #иначе число добавляется в список аргументов

    print(args) # вывод всех аргументов
    if len(args) <= 1: # если их кол-во меньше или равно 1, то вычисления невозможны и функция возвращает None
        return

    action = input("action: ") # ввод действия
    
    try:
        res = calculate(*args, action=action, **PARAMS)
    except Exception: # проверка на типы введенных данных и деление на 0
        print("Ошибка вычисления. Результат не определен") 
    else:
        print_results(*args, action=action, result=res)


def calculate(*args, action=None, **kwargs):
    ''' Главная функция приложения калькулятор, в которой производятся все вычисления, 
    а также запись в историю вычислений. Результат приводится к заданному типу данных и округляется до заданного количества знаков

    >>> calculate(*(1,3,5)), action = "+", **PARAMS)
    9.0
    >>> calculate(*(6,0,3), action = "-", **PARAMS
    3.0
    >>> calculate(*(30, 2, 2), action = "/", **PARAMS)
    7.5
    >>> calculate(*(8, 5, 0.5), action = "*", **PARAMS)
    20.0
    '''

    load_params() # вызов функции по загрузке параметров из файла
    global result # глобальная, чтобы ее было видно в циклах 
    precision = convert_precision(kwargs['precision']) # выгрузка значения точности из файла
    output_type = kwargs['output_type'] # выгрузка значения типа результата из файла

    if action == '+': # действия для сложения
        result = sum(args) # встроенная функция для списков
        if type(result) is not output_type: # приведение к нужному типу, если он уже не принадлежит к нему
            result = output_type(result)
        result = round(result, precision) # округление с использованием значения полученного в начале функции от функции convert_precision

    if action == '-':# действия для вычитания
        result = args[0] # берем за первое значение результата нулевой элемент массива
        for n in args[1:(len(list(args)))]: #перебираем элементы массива с 1 по последний, вычитая каждый из result
            result -= n
        if type(result) is not output_type: # приведение к нужному типу, если он уже не принадлежит к нему
            result = output_type(result)
        result = round(result, precision) # округление с использованием значения полученного в начале функции от функции convert_precision

    if action == '*': # действия для умножения
        result = 1
        for n in args: # умножаем каждый элемент массива друг для друга
            result *= n
        if type(result) is not output_type: # приведение к нужному типу, если он уже не принадлежит к нему
            result = output_type(result)
        result = round(result, precision) # округление с использованием значения полученного в начале функции от функции convert_precision

    if action == '/': # действия для деления
        result = args[0] # берем за начальное значение результата нулевой элемент
        if 0 in args[1:len(args)]: # если в списке, начиная с 1 элемента, содержится 0, то деление невозможно
            return 'Деление невозможно'
        else:
            for n in args[1:(len(list(args)))]: # делим каждый элемент друг на друга
                result /= n
        if type(result) is not output_type: # приведение к нужному типу, если он уже не принадлежит к нему
            result = output_type(result)
        result = round(result, precision) # округление с использованием значения полученного в начале функции от функции convert_precision
    
    write_log(*args, action=action, result = result) # вывод данных в файл с историей вычислений с помощью импортированной функции
    return result


if __name__ == "__main__":
    load_params() # загрузка параметров, используемых при вычислениях, из внешнего файла
    user_input() # вызов функции пользовательского ввода

    # класс с тестами, то что после запятой должно вывестись, иначе будет ошибка теста
    class TestCalculate(unittest.TestCase):
        
        def test_summ(self): # тест суммы
            self.assertEqual((calculate(*(1.8, 4.3, 3.0, 8), action="+", **PARAMS)), 17.1)
        
        def test_difference(self): # тест разности 
            self.assertEqual((calculate(*(11.3, 5, 2.7), action="-", **PARAMS)), 3.6)
            self.assertEqual((calculate(*(4.2, 1.5, 9), action = "-", **PARAMS)), -6.3)
        
        def test_multiplication(self): # тест умножения
            self.assertEqual((calculate(*(3.5, 4, 5.7),action="*", **PARAMS)), 79.8)

        def test_division(self): # тест деления
            self.assertEqual((calculate(*(42, 6.0, 7), action="/", **PARAMS)), 1.0)

        def test_errors(self): # тест ошибок
            with self.assertRaises(Exception):
                calculate(*(12,0), action="/", **PARAMS)
                calculate(*('',5), action="+", **PARAMS)

        def test_precision(self): # тест перевода точности
            self.assertEqual(convert_precision(0.000001), 6)
            self.assertEqual(convert_precision(0.0001), 4)

        def test_file(self): # тест соответствия имени файла
            assert PARAMS.get('dest') == 'output.txt', "Имя файла для записи истории вызовов функции calculate должно быть output.txt"
    
    unittest.main() # вызов функции тестов