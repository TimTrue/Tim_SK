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