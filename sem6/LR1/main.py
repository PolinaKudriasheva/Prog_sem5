from typing import List
from mathstats import MathStats

FILE = 'Retail.csv'
FILE2 = 'MarketingSpend.csv'


def main():
    # запускающая функция
    data = read_data(FILE)
    c = count_invoice(data[:5])
    print(f'Всего инвойсов (invoices): {c}')  # 2
    c = count_invoice(data[:11])
    print(f'Всего инвойсов (invoices): {c}')  # 5
    c = count_invoice(data)
    print(f'Всего инвойсов (invoices): {c}')  # 16522

    data2 = MathStats(FILE2)
    slice_test1 = data2.data[:2]

    print(data2.get_mean(slice_test1))  # (4500.0, 2952.43)

    print(count_different_values(data, 'InvoiceNo'))
    print(get_total_quantity(data, 21421))


def read_data(file: str) -> List[dict]:
    # считывание данных и возвращение значений в виде списка из словарей
    import csv
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for _r in reader:
            row = _r
            # row = {
            #     'InvoiceNo': _r['InvoiceNo'],
            #     'InvoiceDate': _r['InvoiceDate'],
            #     'StockCode': int(_r['StockCode']),
            #     'Quantity': int(_r['Quantity'])
            # }
            data.append(row)
    return data


def count_invoice(data: List[dict]) -> int:
    count = 0
    # 1. Создаем список виденных инвойсов (пустой), пробегаемся по
    # data и если в списке нет очередного инвойса, то добавляем его туда
    # в конце считаем сколько элементов в нем есть.

    # 2. Создаем множество и добавляем туда по очереди все встреченные
    # элементы. Поскольку это множество, инвойсы в нем не будут
    # повторяться. В конце считаем сколько элементов.

    # 3. Counter
    from collections import Counter

    # Реализуем получение номер invoices и помещение их в список
    # Переписать через генератор списка
    invoices = []
    for _el in data:
        invoices.append(_el['InvoiceNo'])

    count = len(Counter(invoices))
    return count


def count_different_values(data: List[dict], key: str) -> int:
    """
    Функция должна возвращать число различных значений для столбца key в списке data
    key - InvoiceNo или InvoiceDate или StockCode
    """

    k = 0
    t = -1
    for _el in data:
      if (t != _el[key]):
        k += 1
        t = _el[key]     
      
    return k


def get_total_quantity(data: List[dict], stock_code: int) -> int:
    """
    Возвращает общее количество проданнорго товара для данного stock_code
    """
    result = 0
    for _el in data:
      if (int(_el["StockCode"]) == stock_code):
        result += int(_el["Quantity"])
      
    return result


if __name__ == "__main__":
    main()
