def print_results(*args, action=None, result=None):
    """
    Вывод результатов вычислений в табличном виде

    Функция принимает переменное число значений, которые нужно вывести в табличном виде. 
    Последний аргумент в упакованном кортеже - результат вычислений, 
    предпоследний - действие, которое выполнилось,
    остальные — аргументы, с которыми это действие выполнилось.
    """

    operands = args[:len(args)] # ввод аргументов в локальный список operands
    print('inp_args in pretty mode', operands, action, result) # вывод аргументов, действия и результата

    def argsPrint(operands): # функция сбора в список аргументов, разделенных прямыми слешами
        lst=[]
        for i in operands:
            lst.append(f"| {i} |")
        return lst 
    
    def actionPrint(operands, action): # функция сбора полного уравнения
        lst=[]
        for i in list(operands[0:-1]):
            lst.append(f"{i} {action}")
        lst.append(f"{operands[-1]}")
        return lst

    arg_list=(" ".join((argsPrint(operands)))) # соединяем список аргументов в строку
    action_list=(" ".join(actionPrint(operands, action))) # соединяем список аргументов со знаками в строку
    st = f"{arg_list} {action_list} = {result} |" # конечная строка
    print('-' * len(st)) # верхняя граница таблицы
    print(st) # строка вывода
    print('-' * len(st)) # нижняя граница таблицы

def write_log(*args, action=None, result=None, file='calc-history.log.txt'):
    # функция вывода истории в файл, по умолчанию calc-history.log.txt
    from datetime import datetime
    f = open(file, mode='a', errors='ignore')
    f.write(f"{datetime.now()} | {action} | {args} = {result} \n") # вывод даты, времени, действия, аргументов и результата
    f.close()