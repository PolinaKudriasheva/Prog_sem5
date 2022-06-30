# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 2
"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы: 
1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
3. Посчитайте долю (процент) погибших на параходе (число и процент)?
4. Какие доли составляли пассажиры первого, второго, третьего класса?
5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром Survived;
2) полом человека и параметром Survived;
3) классом, в котором пассажир ехал, и параметром Survived.
7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.
9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
Для вычисления 3, 4, 5, 6, 7, 8 используйте тип данных float с точностью два знака в дробной части. 
"""

import pandas as pd  # импортирование библиотеки для считывания данных
from numpy import isnan  # импортирование функции isnan для проверки на "not a number"

# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pd.read_csv('train.csv', index_col="PassengerId")
mark_spend = pd.read_csv('MarketingSpend.csv')

# TODO #1
def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """

    n_male, n_female = data['Sex'].value_counts() # функция считает количество различных уникальных значений в серии
    return f"{n_male}, {n_female}" # форматированный вывод результатов


# TODO #2
def get_port_distrib(data):
    """  
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """

    port_S, port_C, port_Q = data['Embarked'].value_counts() # функция считает количество различных уникальных значений в серии
    return f"{port_S}, {port_C}, {port_Q}" # форматированный вывод результатов


# TODO #3
def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """

    # получение количества уникальных элементов
    # нужные нам данные (кол-во умерших) находятся под индексом 0
    n_died = data['Survived'].value_counts()[0]

    # параметр normalize позволяет возвращать относительные частоты уникальных значений
    # это значение нужно умножить на 100, чтобы получить проценты
    perc_died = data['Survived'].value_counts(normalize=True)[0] * 100

    return f"{n_died}, {perc_died:.2f}%" # форматированный вывод с точностью до 2 знаков после запятой


# TODO #4
def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?    
    """
    # параметр normalize позволяет возвращать относительные частоты уникальных значений
    # каждое из этих значений умножаем на 100 для получения процентов
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = data['Pclass'].value_counts(normalize=True) * 100 

    return f"{n_pas_f_cl:.2f}, {n_pas_s_cl:.2f}, {n_pas_t_cl:.2f}" # форматированный вывод с точностью до 2 знаков после запятой


# TODO #5
def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """
    
    # пустые списки для значений параметров SibSp и Parch
    sibsp = []
    parch = []

    i = 0  # счётчик для цикла
    while i < len(data): # цикл будет выполняться, пока счётчик меньше длины наших данных
        
        # data.iloc - обращение к данным
        if not(isnan(data.iloc[i]['SibSp'])): # проверка на NaN параметра SibSp
            sibsp.append(data.iloc[i]['SibSp']) # добавление значения SibSp в список
            parch.append(data.iloc[i]['Parch']) # добавление значения Parch в список
        i += 1

    # преобразование полученных списков в серии, чтобы можно было провести нужные вычисления
    sibsp, parch = pd.Series(sibsp), pd.Series(parch) 

    # вычисление корреляции
    corr_val = sibsp.corr(parch)
    return f"{corr_val:.2f}"


# TODO #6-1
def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - возрастом и параметром Survived;
    """
    
    # аналогично функции выше, разница в параметрах - Age и Survived
    age = []
    surv = []
    i = 0
    while i < len(data):

        if not(isnan(data.iloc[i]['Age'])):
            age.append(data.iloc[i]['Age'])
            surv.append(data.iloc[i]['Survived'])
        i += 1

    age, surv = pd.Series(age), pd.Series(surv)

    corr_val = age.corr(surv)
    return f"{corr_val:.2f}"


# TODO #6-2
def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - полом человека и параметром Survived;
    """

    # аналогично функции выше, разница в параметрах - Sex и Survived
    sex = []
    surv = []
    i = 0
    while i < len(data):

        if not(isnan(data.iloc[i]['Survived'])):

            # для вычисления корреляции нужны числовые значения
            # поэтому с помощью условий преобразуем male в числа 0, а female - в 1
            if data.iloc[i]['Sex'] == "male":
                sex.append(0)
            else:
                sex.append(1)

            surv.append(data.iloc[i]['Survived'])
        i += 1

    sex, surv = pd.Series(sex), pd.Series(surv)

    corr_val = sex.corr(surv)
    return f"{corr_val:.2f}"


# TODO #6-3
def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    - классом, в котором пассажир ехал, и параметром Survived.
    """

    # аналогично функции выше, разница в параметрах - Pclass и Survived
    pclass = []
    surv = []
    i = 0
    while i < len(data):

        if not(isnan(data.iloc[i]['Pclass'])):
            pclass.append(data.iloc[i]['Pclass'])
            surv.append(data.iloc[i]['Survived'])
        i += 1

    pclass, surv = pd.Series(pclass), pd.Series(surv)

    corr_val = pclass.corr(surv)
    return f"{corr_val:.2f}"


# TODO #7
def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """

    # функция mean считает среднее значение, а функция median - медиану
    mean_age, median = data['Age'].mean(), data['Age'].median()
    return f"{mean_age:.2f}, {median:.2f}"


# TODO #8
def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """

    # функция mean считает среднее значение, а функция median - медиану
    mean_price, median = data['Fare'].mean(), data['Fare'].median()
    return f"{mean_price:.2f}, {median:.2f}"


# TODO #9
def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """
    names = [] # пустой список для имён

    # проходимся по данным
    for i in data.iloc:
        if i['Sex'] == "male": # нам нужны только мужские имена

            # обращаемся к имени
            # partition делит строку на 3 части - то, что стоит до шаблона, сам шаблон и то, что после шаблона
            # нам нужно то, что после точки - после слов Mr. и Master. как раз стоят мужские имена
            name = i['Name'].partition('. ')[2] 
            names.append(name) # добавляем обрезанное имя в список

    # находим наиболее встречающееся имя в списке
    # аргумент key нужен для упорядочивания, в данном случае оно поможет найти именно наиболее встречающееся имя
    # set - множество, где хранятся уникальные значения
    result = max(set(names), key = names.count) 
    return f"{result}"


# TODO #10
def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """

    # пустые списки для хранения имён
    male = []
    female = []

    for i in data.iloc:

        # выбираем имена по мужскому полу и возрасту
        if i['Age'] > 15 and i['Sex'] == 'male':
            # метод partition - аналогично выше
            # split - разбиваем строку на список
            name = i['Name'].partition('. ')[2].split(' ')
            male.append(name[0]) # берём первую строку из списка - там содержится имя

        # выбираем имена по женскому полу и возрасту
        elif i['Age'] > 15 and i['Sex'] == 'female':
            
            # женские имена могут быть заключены в скобки - поэтому нужно изъять их оттуда
            if '(' in i['Name']:
                # разделяем имя на 3 части, берём то, что после скобки и обрезаем закрывающую скобку
                name = i['Name'].partition('(')[2].rstrip(')').split(' ')
            
            # на случай, если имена не заключены в скобки
            else:
                name = i['Name'].partition('. ')[2].split(' ')
            
            female.append(name[0])

    # нахождение наиболее частых - аналогично выше
    popular_male_name = max(set(male), key = male.count)
    popular_female_name = max(set(female), key = female.count)
    
    return f"{popular_male_name}, {popular_female_name}"

'''
Часть 2. Для набора данных из лабораторной работы 1 посчитать средние значения, 
медианы, максимальные и минимальные значения для столбцов Offline Spend, Online Spend.
'''

# функция mean считает среднее значение, а функция median - медиану
def find_offline_mean_median(data):
    mean, median = data['Offline Spend'].mean(), data['Offline Spend'].median()
    return f"{mean:.2f}, {median:.2f}"


def find_online_mean_median(data):
    mean, median = data['Online Spend'].mean(), data['Online Spend'].median()
    return f"{mean:.2f}, {median:.2f}"


# функция max считает максимальное значение, а функция min - минимальное
def find_offline_max_min(data):
    max, min = data['Offline Spend'].max(), data['Offline Spend'].min()
    return f"{max}, {min}"


def find_online_max_min(data):
    max, min = data['Online Spend'].max(), data['Online Spend'].min()
    return f"{max}, {min}"


if __name__ == "__main__":
    # вывод результатов
    # 1 часть
    print('1: ', get_sex_distrib(data))
    print('2: ', get_port_distrib(data))
    print('3: ', get_surv_percent(data))
    print('4: ', get_class_distrib(data))
    print('5: ', find_corr_sibsp_parch(data))
    print('6.1: ', find_corr_age_survival(data))
    print('6.2: ', find_corr_sex_survival(data))
    print('6.3: ', find_corr_class_survival(data))
    print('7: ', find_pass_mean_median(data))
    print('8: ', find_ticket_mean_median(data))
    print('9: ', find_popular_name(data))
    print('10: ', find_popular_adult_names(data))

    # 2 часть
    print("Offline: среднее и медиана")
    print(find_offline_mean_median(mark_spend))
    print("Online: среднее и медиана")
    print(find_online_mean_median(mark_spend))
    print("Offline: максимальное и минимальное")
    find_offline_max_min(mark_spend)
    print("Online: максимальное и минимальное")
    find_online_max_min(mark_spend)

#-------------------------------------------------------
  
# тесты
# 1
def test_get_sex_distrib():
    assert get_sex_distrib(data) == "577, 314"

# 2
def test_get_port_distrib():
    assert get_port_distrib(data) == "644, 168, 77"

# 3
def test_get_surv_percent():
    assert get_surv_percent(data) == "549, 61.62%"

# 4
def test_get_class_distrib():
    assert get_class_distrib(data) == "55.11, 24.24, 20.65"

# 5
def test_find_corr_sibsp_parch():
    assert find_corr_sibsp_parch(data) == "0.41"

# 6.1
def test_find_corr_age_survival():
    assert find_corr_age_survival(data) == "-0.08"

# 6.2
def test_find_corr_sex_survival():
    assert find_corr_sex_survival(data) == "0.54"

# 6.3
def test_find_corr_class_survival():
    assert find_corr_class_survival(data) == "-0.34"

# 7
def test_find_pass_mean_median():
    assert find_pass_mean_median(data) == "29.70, 28.00"

# 8
def test_find_ticket_mean_median():
    assert find_ticket_mean_median(data) == "32.20, 14.45"

# 9
def test_find_popular_name():
    assert find_popular_name(data) == "John"

# 10
def test_find_popular_adult_names():
    assert find_popular_adult_names(data) == "William, Anna"
