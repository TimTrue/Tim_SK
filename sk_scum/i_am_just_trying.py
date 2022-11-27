# PYTHON-9
# 2. Модуль Collections. Counter и defaultdict

# Импортируем объект Counter из модуля collections
from collections import Counter
# Создаём пустой объект Counter
c = Counter()

#Подсчет уникальных значений
cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c = Counter(cars)
print(c)

#Cколько раз встретился конкретный элемент
print(c['black'])

#Вывести только количество
print(c.values())

#Сумма значений количества
print(sum(c.values()))


#Статистика по цветам машин в разных городах
cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

#Счетчик уникальных значений
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
print(counter_moscow)
print(counter_spb)

#Чтобы узнать, сколько машин разных цветов встретилось в двух городах, можно сложить два исходных счётчика и получить новый счётчик
print(counter_moscow + counter_spb)

#Чтобы узнать разницу между объектами Counter, необходимо воспользоваться функцией subtract
counter_moscow.subtract(counter_spb)
print(counter_moscow)

#Для вывода только положительных значений просто вычетаем

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
print(counter_moscow - counter_spb)

# Чтобы получить список всех элементов, которые содержатся в Counter, используется функция elements(). 
# Она возвращает итератор, поэтому, чтобы напечатать все элементы, распакуем их с помощью *
print(*counter_moscow.elements())

# Чтобы получить список уникальных элементов, достаточно воспользоваться функцией list():
print(list(counter_moscow))

# С помощью функции dict() можно превратить Counter в обычный словарь:
print(dict(counter_moscow))

#Функция most_common() позволяет получить список из кортежей элементов в порядке убывания их встречаемости:
print(counter_moscow.most_common())

# В неё также можно передать значение, которое задаёт желаемое число первых наиболее частых элементов, например, 2:
print(counter_moscow.most_common(2))

# Функция clear() позволяет полностью обнулить счётчик:
counter_moscow.clear()
print(counter_moscow)

#DEFAULTDICT
# У нас есть список из кортежей с фамилиями студентов и их учебными группами
students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]

# Создадим defaultdict, в котором при обращении по несуществующему ключу будет автоматически создаваться новый список. 
# Для этого при создании объекта defaultdict в круглых скобках передадим параметр list:
from collections import defaultdict
groups = defaultdict(list)

# Сохраним эти данные в словаре, в котором ключами будут номера групп, а элементами — списки студентов.
for student, group in students:
    groups[group].append(student)
 
print(groups)


# 3. Модуль Collections. Deque и OrderedDict

# Задание 3.2
# Дан список из кортежей temps. 
# На первом месте в кортеже указан год в виде строки, а на втором — средняя температура января в Петербурге в указанном году.
# Напишите функцию check(temps), которая будет выводить словарь, в котором ключи — годы, а значения — показатели температуры. 
# Ключи необходимо отсортировать в порядке убывания соответствующих им температур.

from collections import OrderedDict
temps =  [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

def check(temps):
    # Создаем OrderDict и сортируем по значению температуры с использованием обратной сортировки reverse
    order_temp = OrderedDict(sorted(temps, key=lambda x: x[1], reverse=True))
    return order_temp

print(check(temps))

#DEQUE

# # Заданий 3.5-3.7
# from hidden import users
# # Пишите здесь команды, который помогут
# # найти ответы на вопросы
# from collections import deque
# dq_users = deque(users)
# # Извлеките элемент из начала очереди. Запишите полученное значение элемента в качестве ответа
# dq_users.popleft()
# # В уже модифицированной очереди переместите пять элементов из начала очереди в её конец.
# dq_users.rotate(-5)
# # Извлеките последний элемент из очереди. Запишите полученное число в качестве ответа.
# dq_users.pop()
# # Сколько задач с тем номером, что был извлечён в предыдущем задании, осталось в модифицированной очереди?
# print(dq_users.count(8))


# Pyth 9 4. Модуль Collections. Закрепление знаний
# ЗАДАНИЕ 4.3
# Напишите функцию brackets(line), которая определяет, является ли последовательность из круглых скобок line правильной.

from collections import deque

def brackets(line):
    dq_line = deque()
    for l in line:
        if l == '(':
            dq_line.append('(')
        elif l == ')':
            if len(dq_line) == 0:
                return False
            dq_line.pop()
    if len(dq_line) == 0:
        return True
    else:
        return False

print(brackets('(()())'))

# Задание 4.4
# В переменных center, south и north хранятся списки из перечней купленных позиций в трёх торговых точках, расположенных в разных районах города.
# Вначале избавьтесь от излишней вложенности: 
center = [['Milk', 'Bread'], ['Meat']]
south = [['Milk', 'Bread'], ['Meat', 'Cake']]
north = [['Brad', 'Egg'], ['Milk'], ['Water']]

# В каждой переменной (center, south, north) должен храниться объединённый список купленных товаров без разбиения по чекам.
center_list = [position for check in center for position in check]
south_list = [position for check in south for position in check]
north_list = [position for check in north for position in check]

print(center_list)
print(south_list)
print(north_list)

# После этого определите, в каком магазине было куплено больше всего товаров
print(len(north_list))
print(len(south_list))
print(len(center_list))

#Теперь получите объекты-счётчики (Counter) из каждого полученного в предыдущем задании списка покупок и сохраните их в отдельные переменные.
from collections import Counter

c = Counter(center_list)
s = Counter(south_list)
n = Counter(north_list)

#Сколько раз покупали самый редкий товар в магазине north
print(n.most_common()[-1])

# Выберите товар, который в магазине center покупали чаще, чем в магазине north
print(c - n)

#Есть ли такой товар, который в одном из магазинов покупали чаще, чем в двух других вместе взятых
print("Center", c - (n + s))
print("North", n - (c + s))
print("South", s - (c + n))

#Определите суммарное число продаж каждого товара во всех магазинах
c_sum = c + n + s
print(c_sum)

#Сколько раз был куплен второй по популярности товар?
print(c_sum.most_common()[1])

# Задание 4.9
# Дан список кортежей ratings с рейтингами кафе. Кортеж состоит из названия и рейтинга кафе
ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
          ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
          ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

# Необходимо отсортировать кортеж по убыванию рейтинга. 
# Если рейтинги совпадают, то отсортировать кафе дополнительно по названию в алфавитном порядке.
ratings.sort(key=lambda x: (-x[-1], x[0]))
#print(ratings)

# Получите словарь cafes с упорядоченными ключами из отсортированного списка, 
# где ключи — названия кафе, а значения — их рейтинг.
from collections import OrderedDict

cafes = OrderedDict(ratings)
#print(cafes)

# Задание 4.10
# Напишите функцию task_manager, которая принимает список задач для нескольких серверов. 
# Каждый элемент списка состоит из кортежа (<номер задачи>, <название сервера>, <высокий приоритет задачи>)
tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

# Для словаря используйте defaultdict, для очереди — deque.
from collections import defaultdict
from collections import deque

def task_manager(tasks):
    # Функция должна создавать словарь и заполнять его задачами по следующему принципу: 
    servers = defaultdict(deque)
    # Название сервера — ключ, по которому хранится очередь задач для конкретного сервера
    for task in tasks:
        # Если приоритет высокий, добавить номер в начало.
        if task[-1]:
            servers[task[1]].appendleft(task[0])
        # Если поступает задача без высокого приоритета (последний элемент кортежа — False), добавить номер задачи в конец очереди.
        else:
            servers[task[1]].append(task[0])
    # Функция возвращает полученный словарь с задачами.
    return servers

print(task_manager(tasks))

# 7. Модуль NumPy. Действия с массивами
# Задание 7.2
import numpy as np

# Вам дан массив mystery
mystery = np.array([[-13586,  15203,  28445, -27117,  -1781, -17182, -18049],
       [ 25936, -30968,  -1297,  -4593,   6451,  15790,   7181],
       [ 13348,  28049,  28655,  -6012,  21762,  25397,   8225],
       [ 13240,   7994,  32592,  20149,  13754,  11795,   -564],
       [-21725,  -8681,  30305,  22260, -17918,  12578,  29943],
       [-16841, -25392, -17278,  11740,   5916,    -47, -32037]],
      dtype=np.int16)

# В переменную elem_5_3 сохраните элемент из 5 строки и 3 столбца
elem_5_3 = mystery[4, 2]
#print('elem_5_3', elem_5_3)

# В переменную last сохраните элемент из последней строки последнего столбца
last = mystery[-1, -1]
#print('last', last)

# В переменную line_4 сохраните строку 4
line_4 = mystery[3]
#print('line_4', line_4)

# В переменную col_2 сохраните предпоследний столбец
col_2 = mystery[0: ,-2]
#print('col_2', col_2)

# Из строк 2-4 (включительно) получите столбцы 3-5 (включительно). Результат сохраните в переменную part
part = mystery[1:4, 2:5]
#print('part', part)

# Сохраните в переменную rev последний столбец в обратном порядке
rev = mystery[0:, -1][::-1]
#print('rev', rev)

# Сохраните в переменную trans транспонированный массив
trans = mystery.transpose()
#print('trans', trans)

# Задание 7.4 
import numpy as np

# Вам дан массив mystery:
mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)

# Получите булевый массив nans_index с информацией о np.nan в массиве mystery: 
# True - значение пропущено, False - значение не пропущено
nans_index = np.isnan(mystery)
#print('nans_index', nans_index)

# В переменную `n_nan сохраните число пропущенных значений
n_nan = len(mystery[np.isnan(mystery)])
#print('n_nan', n_nan)

# Скопируйте массив mystery в массив mystery_new. Заполните пропущенные значения в массиве mystery_new нулями
#mystery_new = mystery.copy()
mystery_new = mystery
mystery_new[np.isnan(mystery_new)] = 0
#print('mystery_new', mystery_new)

# Поменяйте тип данных в массиве mystery на int32 и сохраните в переменную mystery_int
mystery_int = np.int32(mystery)
#print('mystery_int', mystery_int)

# Отсортируйте значения в массиве по возрастанию и сохраните результат в переменную array
array = np.sort(mystery)
#print('array', array)

# Сохраните в массив table двухмерный массив, полученный из массива array. 
# В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть по столбцам
table = array.reshape((5, 3), order='F')
#print('table', table)

# Сохраните в переменную col средний столбец из table
col = table[:, 1]
#print('col', col)

# 8. Модуль NumPy. Операции с векторами

# Задания 8.4-8.6
# Векторы в геометрии называются сонаправленными, если они коллинеарны и их направления совпадают:
# сумма длин сонаправленных векторов должна быть равной длине суммы двух векторов.

import numpy as np

# Даны векторы
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])

# Найдите пару сонаправленных векторов
print('a и b сонаправленные векторы', (np.linalg.norm(a) + np.linalg.norm(b)) == np.linalg.norm(a + b))
print('a и c сонаправленные векторы', (np.linalg.norm(a) + np.linalg.norm(c)) == np.linalg.norm(a + c))
print('b и c сонаправленные векторы', (np.linalg.norm(b) + np.linalg.norm(c)) == np.linalg.norm(b + c))
    
# Найдите пару векторов, расстояние между которыми больше 100
print('расстояние между a и b > 100', (np.linalg.norm(a-b) > 100))
print('расстояние между a и c > 100', (np.linalg.norm(a-c) > 100))
print('расстояние между b и c > 100', (np.linalg.norm(b-c) > 100))

# Найдите пару перпендикулярных векторов с помощью скалярного произведения (оно должно быть равно нулю)
print('a и b перпендикулярны', (np.dot(a, b) == 0))
print('a и c перпендикулярны', (np.dot(a, c) == 0))
print('b и c перпендикулярны', (np.dot(b, c) == 0))

# Задания 8.7-8.10
# БАЗОВЫЕ СТАТИСТИЧЕСКИЕ ФУНКЦИИ ДЛЯ ВЕКТОРОВ

mystery = np.array([481,  18, 308,  13, 652, 391,  63,  62 ,353, 111, 805, 251,  36, 544, 600, 799, 283, 880,
 470, 599, 814, 507, 242, 650, 180, 860, 979, 298, 621, 197, 572, 976, 905, 427, 119, 905,
  64, 430, 742, 563, 382, 211, 228, 760, 567, 366, 103, 409, 211, 952,   5, 493, 151, 267,
 517, 495, 375,  80, 341,  39, 560,  85, 490,  44,  17, 151,  42, 688, 648, 501, 437, 154,
  66, 28, 921, 642, 196, 719, 208, 492, 538, 687, 841, 933, 386, 719, 114, 261, 838, 228,
 120, 508, 316, 476, 233, 902, 698, 471, 604, 172, 993, 790, 557, 129, 446,  64, 317, 997,
 509, 710, 909, 147, 228, 595, 188, 246, 728, 509, 365, 139, 773, 426, 929, 888, 534, 513,
 666,  77, 299, 943, 985, 588, 137,  31, 385, 405, 980, 854, 327, 714, 318, 909, 803, 334,
 130, 949, 532, 640, 820, 975, 889, 240, 878, 294, 899, 488, 639, 961, 819, 649, 939, 163,
 209, 879, 479, 573, 557,  25, 783, 332, 311, 425, 140, 678, 766, 492, 234, 316, 811, 447,
 772, 325, 640, 387, 858, 208, 739, 870, 227, 385,  24, 286,  22, 599, 951, 994, 457,  99,
 238, 172, 549, 932, 412, 545, 713,  19, 785, 931, 684, 333, 630, 752, 191, 949, 200, 361,
 887, 243, 753, 600, 635, 243, 173, 249, 294, 583, 106, 772, 848, 387, 874, 321, 562,  96,
 211, 561, 918, 868, 206, 745, 710, 869, 387, 600, 726, 179, 336, 806, 392, 612])

import numpy as np

# Найдите минимальное значение в массиве mystery
print('min', np.min(mystery))

# Найдите среднее значение массива. Ответ не округляйте
print('mean', np.mean(mystery))

# Найдите медиану массива.
print('median', np.median(mystery))

# Найдите стандартное отклонение значений в массиве. Ответ округлите до сотых.
print('std', round(np.std(mystery),2))


# 9. Модуль NumPy. Случайные числа
# Задание 9.6

import numpy as np

# Задайте seed = 2021.
np.random.seed(2021)

# В simple сохранте случайное число в диапазоне от 0 до 1
simple = np.random.uniform(0, 1)
# print (simple)

# Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их в переменную randoms
randoms = np.random.uniform(-150, 2021, size = 120)
# print(randoms)

# Получите массив из случайных целых чисел от 1 до 100 (включительно) из 3 строк и 2 столбцов. Сохраните результат в table
table = np.random.randint(1, 101, size = (3,2))
# print(table)

# В переменную even сохраните четные числа от 2 до 16 (включительно)
even = np.arange(2, 17, 2)
# print(even)

# Скопируйте even в переменную mix. Перемешайте числа в mix так, чтобы массив изменился
mix = even
np.random.shuffle(mix)
# print(mix)

# Получите из even 3 числа без повторений. Сохраните их в переменную select
select = (np.random.choice(even, size = 3, replace= False))
# print(select)

# Получите переменную triplet, которая должна содержать перемешанные значения из массива select (сам select измениться не должен)
triplet = np.random.permutation(select)
# print(triplet)


# 10. Модуль NumPy. Закрепление знаний

import numpy as np

# Задание 10.5
# Получите сумму чисел, сохранённых в переменных a и b.

a = np.int32(2147483548)
b = np.int32(2147471336)

print(np.int64(a) + np.int64(b))

# ЗАДАНИЕ 10.6

# Напишите функцию get_chess(a), которая принимает на вход длину стороны квадрата a и возвращает двумерный массив формы (a, a), 
# заполненный 0 и 1 в шахматном порядке. 
# В левом верхнем углу всегда должен быть ноль

def get_chess(a):
    zeros_2d = np.zeros((a, a))
    zeros_2d[::2, 1::2] = 1
    zeros_2d[1::2, ::2]  = 1
    return zeros_2d

# print(get_chess(5))

# ЗАДАНИЕ 10.7
# Вы разрабатываете приложение для прослушивания музыки.
# Пользователю может настолько понравиться перемешанная версия плейлиста, что он захочет сохранить его копию.
# Вы хотите сохранять тот seed, с которым он был сгенерирован.

# Для этого напишите функцию shuffle_seed(<array>),  
# которая принимает на вход массив из чисел, генерирует случайное число для seed в диапазоне от 0 до 2**32 - 1 (включительно) и возвращает кортеж: 
# перемешанный с данным seed массив (исходный массив должен оставаться без изменений), 
# а также seed, с которым этот массив был получен.

def shuffle_seed(array):
    import numpy as np
    seed = np.random.randint(2**31) # 2*32-1
    np.random.seed(seed)
    choice = np.random.choice(array, size = len(array), replace=False)
    return choice, seed

array = [1, 2, 3, 4, 5]
print('playlist', shuffle_seed(array))

# Задание 10.8
# Напишите функцию min_max_dist(*vectors), которая принимает на вход неограниченное число векторов через запятую. 
# Гарантируется, что все векторы, которые передаются, одинаковой длины.

def min_max_dist(*vectors):
    import numpy as np
    # список расстояний между i и i+1
    dist_list = list()
    # цикл для i-го сравневаемого значения
    for i in range(len(vectors)):
        # цикл для i+1 сравневомого значения
        for j in range(i+1, len(vectors)):
            # определение расстояния и добавление в список
            dist_list.append(np.linalg.norm(vectors[i] - vectors[j]))
    # Функция возвращает минимальное и максимальное расстояние между векторами в виде кортежа.
    return (min(dist_list), max(dist_list))

vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])

print(min_max_dist(vec1, vec2, vec3))

# Задание 10.9
# Напишите функцию any_normal, которая принимает на вход неограниченное число векторов через запятую. 
# Гарантируется, что все векторы, которые передаются, одинаковой длины.

def any_normal(*vectors):
    import numpy as np
    
    # цикл для i-го сравневаемого значения
    for i in range(len(vectors)):
        # цикл для i+1 сравневомого значения
        for j in range(i+1, len(vectors)):
            # определение перпендикулярности
            if np.dot(i, j) == 0:
                # Функция возвращает True, если есть хотя бы одна пара перпендикулярных векторов.
                return True
    # Иначе возвращает False.
    return False

vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
print(any_normal(vec1, vec2, vec3))


# Задание 10.10
# Напишите функцию get_loto(num), генерирующую трёхмерный массив случайных целых чисел от 1 до 100 (включительно). 
# Это поля для игры в лото.
def get_loto(num):
    import numpy as np
    loto_board = np.random.randint(1, 101, size=(num, 5, 5))
    return loto_board

print(get_loto(3))


# Задание 10.11
# Напишите функцию get_unique_loto(num). Она так же, как и функция в задании 49.9.10, 
# генерирует num полей для игры в лото, однако теперь на каждом поле 5х5 числа не могут повторяться.

def get_unique_loto(num):
    import numpy as np
    choises = np.arange(1, 101)
    loto_board = list()
    for i in range(num):
        loto_board.append(np.random.choice(choises, size = (5, 5), replace = False))
    loto_board = np.array(loto_board)
    return loto_board

print(get_unique_loto(3))