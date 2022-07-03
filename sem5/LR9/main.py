import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, date, timedelta
import requests
from bs4 import BeautifulSoup


def get_currencies(currencies_ids_lst =[ 
            'R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589',
            'R01625', 'R01670', 'R01700J', 'R01710A'
        ]): # получение значений валют, которые передаются списком в функцию

    cur_res_str = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text # отправка запроса на апи и преобрахование ответа в текст
    result = dict()
    # парсим данные и извлекаем необходимые валюты 
    soup = BeautifulSoup(cur_res_str, 'html.parser') 
    valutes = soup.find_all("valute")
    for _v in valutes:
        valute_id = _v['id']
            
        if str(valute_id) in currencies_ids_lst:
            valute_cur_val = _v.find('value').string
            valute_cur_name = _v.find('name').string
            result[valute_cur_name] = valute_cur_val

    return result


# TODO 0 

# Вывести на графике 10 валют (получить по кодам валюты из ЦБС)

cur_vals = get_currencies()
objects = cur_vals.keys()

y_pos = np.arange(len(objects))

# TODO #1 переписать лямбда-функцию из следующей строки через list comprehension 

# или генераторы списков (как мы их называем)
performance = [float(x.replace(',', '.')) for x in cur_vals.values()]
# TODO #2 

#  Подписи должны быть у осей (x, y), у графика, у «рисок» (тиков), 
# столбцы должны быть разных цветов с легендой

# TODO #3 

# Нарисовать отдельный график с колебанием одной (выбранной вами) валюты
# (получить данные с сайта ЦБ за год) и отобразить его наиболее 
# оптимальным образом (типом графика)

def get_currencies_year(currencie_id='R01239'): # функция получения валюты за год

    today = datetime.today() # берём сегодняшнюю дату
    date = today - timedelta(days=365) # находим начальную дату: сегодняшняя - 365 дней
    result = dict()
    valute_name = "Евро"

    while date !=today: # итерируемся по циклу 365 раз, отправляя каждый раз запрос

        day = str(date.day)
        month = str(date.month)

        if len(str(date.day)) == 1: # так как по запросу ожидается формат дд:мм:гггг то стоит проверять является ли число однозначным
            day = '0' + str(date.day) # если является, то приписать к началу 0, иначе в качестве ответа придёт ошибка
        
        if len(str(date.month)) == 1: # аналогично также как и с числом выше
            month = '0' + str(date.month)

        req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', params = {'date_req':day + '/' + month + '/' + str(date.year)}).text # отправка запроса

        soup = BeautifulSoup(req, 'html.parser') # парсинг необходимой валюты
        valutes = soup.find_all("valute")

        for _v in valutes:
            valute_id = _v['id']
                
            if str(valute_id) == currencie_id:
                valute_val = float('.'.join(_v.find('value').string.split(',')))
                result[date.strftime("%d/%m/%Y")] = valute_val

        date = date + timedelta(days = 1) # добавление одного дня к итерируемой переменной

    res = {valute_name:result}
    return res


# TODO #4 

# Отобразить это на одном изображении (2 графика)

plt.bar(y_pos, performance)
plt.xticks(y_pos, objects)
plt.ylabel('Стоимость')
plt.xlabel('Валюта')
plt.title('Курс валют по отношению к рублю')
plt.show()

year_currencies = get_currencies_year()
x = []
y = []

for n in list(year_currencies["Евро"].items()):
    x.append(n[0])
    y.append(n[1])

plt.plot(x,y)
plt.title("Курс евро по отношению к рублю за год")
plt.xlabel('Дата')
plt.ylabel('Значение')
plt.yticks(y[::1])
plt.xticks(x[::1])
plt.show()
