"""
    ИСР 1.1. 
    Разработка скрипта, вычисляющего статистические показатели (среднее значение, дисперсия, среднее квадратичное отклонение) для данных, считанных из CSV-файла.
"""

import csv
from math import sqrt


def mean(data):
    return sum(data) / len(data)


def dispersion(data):
    average = mean(data)
    data_for_disp = [(i - average)**2 for i in data]
    disp = sum(data_for_disp) / (len(data_for_disp))
    return disp


def sigma_sq(data):
    return sqrt(dispersion(data))


def csv_reader(file, col_num):
    reader = csv.reader(file, delimiter=',')
    data = []
    for line in reader:
        data.append(float(line[col_num - 1]))
    return data


def main():
    csv_file = 'data.csv'
    column_number = 3
    with open(csv_file, newline='') as file:
        data = csv_reader(file, column_number)
    print('Среднее значение: ', mean(data))
    print('Дисперсия: ', dispersion(data))
    print('Среднее квадратичное отклонение: ', sigma_sq(data))


main()
