users = [
         [15634602, 15647311, 15619304, 15701354],#'CustomerId'
         ['Hargrave', 'Hill', 'Onio', 'Boni'],#'Surname'
         [619, 608, 502, 699], #'CreditScore'
         ['Female', 'Female', 'Male', 'Female'], #'Gender'
         [42, 41, 42, 39], #'Age'
         [1, 0, 1, 0] #Exited
         ]
#customer_id = users[0]
#surname = users[1]
#credit_score = users[2]
#gender = users[3]
#age = users[4]
#exited = users[5]
#print(customer_id, surname, credit_score, gender, exited)
print(sum(users[2])/len(users[2])) #Расчитает среднее по признаку кредитного рейтинга для ушедших клиентов
print(sum(users[4])/len(users[4])) #Средний возраст всех клиентов
print(users[5].count(1)/len(users[5])*100) #Долю ушедших клиентов
#index_exited = [i for i, x in enumerate(users[5]) if x == 1] #Получение индексов для значений 1 в users[5]; enumerate() - получае индекс и его значение
#print(index_exited)
for i in range(len(users[5])): #через range() создаем список из длины users[5] и тем самым задаем количестов итераций
    if users[5][i] == 1: #ищем значения, равные 1 в users[5]
        print(users[0][i]) #Выводим значения которые подходят под услоавия (Выведет идентификаторы клиентов, которые ушли от банка)

4.6 #Пусть у нас есть некоторая информация о пабликах в сети ВКонтакте. 
#Необходимо организовать код для получения ссылок на аватарки данных пабликов. 
#Все ссылки необходимо оформить во вложенный список [[photo_50, photo_100, photo_200], [photo_50, photo_100, photo_200]]
response = {'response': [{'id': 42565717,
   'name': 'Python',
   'screen_name': 'club42565717',
   'is_closed': 0,
   'type': 'group',
   'members_count': 37319,
   'activity': 'Открытая группа',
   'photo_50': 'https://sun9-127.userapi.com/c845524/v845524906/1a71c2/A2r_4JtmiLQ.jpg?ava=1',
   'photo_100': 'https://sun9-58.userapi.com/c845524/v845524906/1a71c1/2fBtsS0k8XY.jpg?ava=1',
   'photo_200': 'https://sun9-50.userapi.com/c845524/v845524906/1a71c0/Kfo-eQIn0DU.jpg?ava=1'},
                         
  {'id': 3183750,
   'name': 'Веб программист - PHP, JS, Python, Java, HTML 5',
   'screen_name': 'php2all',
   'is_closed': 0,
   'type': 'page',
   'members_count': 117833,
   'activity': 'Программирование',
   'photo_50': 'https://sun9-54.userapi.com/c626421/v626421613/941/HSj4ylRsk8k.jpg?ava=1',
   'photo_100': 'https://sun9-5.userapi.com/c626421/v626421613/940/yKaZLxGShkY.jpg?ava=1',
   'photo_200': 'https://sun9-49.userapi.com/c626421/v626421613/93f/2EygT_FJKWg.jpg?ava=1'}]}
photo = [
         [response['response'][0]["photo_50"], 
          response['response'][0]["photo_100"], 
          response['response'][0]["photo_200"]
         ], 
         [response['response'][1]["photo_50"], 
          response['response'][1]["photo_100"], 
          response['response'][1]["photo_200"]
         ]
        ]
print(photo)

# Запишите условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
if ((a < 45) and (b >= 45) and (c >=45)) or \
    ((a >= 45) and (b < 45) and (c >=45)) or \
    ((a >= 45) and (b >= 45) and (c < 45)):
    print('True')
else:
    print('False')
#Запишите логическое выражение, которое определяет, что число А не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.
d = int(input('Enter another one number: '))
if (-10 <= d <= -1) or (2 <= d <= 15):
    print('False')
else:
    print('True')
#Дано двузначное число. Определите, входит ли в него цифра 5. Попробуйте решить задачу с использованием целочисленного деления и деления с остатком.
e = int(input('Enter another one number >=10 and <100: '))
if (e % 10 == 5) or (e // 10 == 5):
    print('True')
else:
    print('False')
#Проверьте, все ли элементы в списке являются уникальными.
f = list(input('Enter another one number for list:'))
if (len(f) == len(set(f))): #set - создает множество уникальных значений
    print('True')
else:
    print('False')
#Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом (читается одинаково слева направо и справа налево).
g = str(input('Enter eight-digit number:'))
if g == g[::-1]:
    print('True')
else: 
    print ('False')

# Введите здесь ваш код
#Ход королевы. Шахматный ферзь ходит по диагонали, горизонтали или вертикали. 
#Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом. 
#В случае, если хотя бы одно из введенных чисел не лежит в диапазоне от 1 до 8, выведите строку "Ошибка!".
x_current = 8
y_current = 3
x_new = int(input('Enter new x '))
y_new = int(input('Enter new y '))

if (1 < x_new <= 8) or (1 < y_new <= 8):
    if (x_current == x_new) and (y_current == y_new):
        print('No move')
    elif abs(x_current - x_new) == abs(y_current - y_new):#ход по диагонали
        print('Successful move')
    elif x_current == x_new: #ход по вертикали
        print('Successful move')
    elif y_current == y_new:
        print('Successful move')#ход по горизонтали 
    else:
        print('Unsuccessful move')
else: 
    print('Unsuccessful move')
print('An attempt was made to move the queen from the cell:', (x_current, y_current), 'to the cell:', (x_new, y_new))

#Пользователи бывают разные: прекрасные и безобразные. Предположим, в вашем приложении предусмотрен ввод имени, даты рождения и почты.
#Давайте рассмотрим, какие ошибки могут возникнуть при таком вводе?
name = input('Введите имя: ')
birthday = input('Введите дату рождения в формате год-месяц-день: ')
mail = input('Введите почту: ')

#pyth4 1.2
incomes = [120, 38.5, 40.5, 80]
sum_ = 0
for income in incomes:
    sum_ += income
    #print(sum_)
print(sum_)

#pyth4 1.3
lst = [98, 24, 23, 12, 3]
prod = 1
for value in lst:
    prod *= value
    #print(prod)
print(prod)

#pyth4 1.4 - 1.5
p = 1
n = 5
for i in range(1, n+1):
    p *= i
    print('n = ', i)
    for i in range(1, i+1):
        print("*" * i)
print(p)

#pyth4
weight_of_products = [10, 42.4, 240.1, 101.5, 98, 0.4, 0.3, 15] #список масс товаров
max_weight = 100 #задаём максимальное значение веса груза
num = len(weight_of_products)#вычисляем длина списка
#создаём цикл по последовательности чисел от 0 до num (не включая mum)
for i in range(num): #i — текущее значение последовательности
    #обращаемся к элементу по индексу и сравниваем его с максимумом
    if weight_of_products[i] < max_weight: #если текущий вес меньше максимального,
        #выводим номер груза, массу и отправляем его в легковую машину
        print('Product {}, weight: {} - passenger car'.format(i+1, weight_of_products[i])) 
    else:
        #выводим номер груза, массу и отправляем его в грузовую машину
        print('Product {}, weight: {} - truck'.format(i+1, weight_of_products[i]))

#pyth4        
#список мест, которые хотим посетить
places = [
    'Red Square',
    'Swallow Nest',
    'Niagara Falls',
    'Grand Canyon',
    'Louvre',
    'Hermitage'
] 
#словарь соответствия мест и стран
location = {
    'Red Square': 'Russia',
    'Swallow Nest': 'Russia',
    'Niagara Falls': 'USA',
    'Grand Canyon': 'USA',
    'Louvre': 'France',
    'Hermitage': 'Russia'
}
N = len(places) #вычисляем длину списка
#создаём цикл по списку мест, которые хотим посетить
for i in range(N): #i — текущее значение последовательности
    #places[i] — i-й элемент в списке places
    country = location[places[i]] #получаем страну из словаря location по ключу
    if country != 'Russia': #сравниваем название стран
        places[i] = 'Unavailable' #помечаем место как недоступное
print(places) #выводим результирующий список

#pyth4 1.9
word_list = ['My', 'name', 'is', 'Artem']
sentence = ''
for i in word_list:
    sentence += i + ' '
print(sentence)  

#или
word_list = ['My', 'name', 'is', 'Artem']
n_word = len(word_list)
sentence = ''
for i in range(n_word):
    sentence += word_list[i] + ' '
print(sentence)

#pyth4 1.10
num_list = [1, 10, 3, -5]
num_list.sort()
n = len(num_list)
for i in range(n):
    print(num_list[i])

#pyth4 1.11
my_list = list(range(0, 100, 3))
count_=0
for i in my_list:
    if i % 2 == 0:
        count_ += 1
print(count_)

#pyth4 1.12
my_list = [True, 1, -10, 'hello', False, 'string_1', 123, 2.5, [1, 2], 'another']
count_=0
for i in my_list:
    if type(i) == str:
        count_ += 1
print(count_)

#Pyth4 Распарсить таблицу Вариант 1
temperature = [
    [13, 15, 10],
    [14, 13, 9],
    [8, 9, 6]
]
for i in range(len(temperature)):
    print(temperature[i])
    for g in range(len(temperature[i])):
        print(temperature[i][g])
        
#Pyth4 Распарсить таблицу Вариант 2
temperature = [
    [13, 15, 10],
    [14, 13, 9],
    [8, 9, 6]
]
for row in temperature:
    print(row)
    for elem in row:
        print(elem)

#Pyth4 3.1
# Выводите на экран элементы из таблицы temperature, находящиеся на следующих позициях:
# Первая строка, третий столбец
# Вторая строка, второй столбец
# Третья строка, первый столбец
print (temperature[0][2], temperature[1][1], temperature[2][1])

#Pyth4 3.2
#Пусть пользователь заводит будильники на каждые два часа, начиная с 9 часов утра. 
#Причём будильники должны звонить четырежды в указанный час (интервал 15 минут), например в 11:00, 11:15, 11:30 и 11:45.
#Напишите вложенный цикл, который будет выводить на экран время, в которое прозвенят будильники.

hours = list(range(9, 24, 2))
minutes = list(range(0, 60, 15))
for i in hours:
    for g in minutes:
        print('Alarm is set {}:{}'.format(i, g))
        
s = 'television'
print(s.count('e'))
#Pyth4 3.2
#Дан список строк text_list. 
#Посчитайте, сколько раз во всех строках списка встречается буква 'a'.
text_list = [
    'afbaad',
    'faaf',
    'afaga',
    'agag'
]
a_r = 0
a_e = 0
for i in range(len(text_list)):
    a_e += text_list[i].count('a')
    a_r += a_e
    a_e = 0
print(a_r)    

#Pyth4 3.3
#Найти максимумы в строках таблицы
random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]
max_value_row = []
for i in range(len(random_matrix)):
    max = random_matrix[i][0]
    for g in range(len(random_matrix[i])):
        if random_matrix[i][g] > max:
            max = random_matrix[i][g]
    max_value_row.append(max)
    print(max)
print(max_value_row)

#Pyth4 3.8
#Напишите код, который определяет, является ли вложенный список квадратной матрицей
test_matrix1 = [
    [1, 2, 3],
    [7, -1, 2],
    [123, 2, -1]
]
test_matrix2 = [
    [1, 2, 3],
    [7, -1, 2],
    [123, 2, -1],
    [123, 5, 1]
]
count = 0
for i in range(len(test_matrix1)):
    if len(test_matrix1) == len(test_matrix1[i]):
        count += 1
print(len(test_matrix1) == count)

count = 0
for i in range(len(test_matrix2)):
    if len(test_matrix2) == len(test_matrix2[i]):
        count += 1
print(len(test_matrix2) == count)

#Pyth4 4.3
user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
for i, number in enumerate(user_dynamics): # функция enumerate() используется в цикле for и на каждой его итерации выдаёт индекс элемента и значение.
    if number < 0: #если условие истинно,
        print("Churn value: ", i+1) # выводим количество ушедших в этот день пользователей
        print("Number day: ", number) # выводим номер дня

#Pyth4 4.6
#Допишите программу, которая проверяет гипотезу Сиракуз
#любое натуральное число можно свести к 1, если повторять над ним следующие действия:
#если число чётное, разделить его пополам, т. е. n = n // 2;
#если нечётное — умножить на 3, прибавить 1 и результат разделить на 2, т. е. n = (n * 3 + 1) // 2
n = 18 #задаём число
while True: #создаём бесконечный цикл
    if n % 2 == 0:
        n = n // 2
        #print(n)
    else:
        n = (n * 3 + 1) // 2
        #print(n)
    if n == 1: #если результат равен 1,
        print('Syracuse hypothesis holds') #выводим утвердительное сообщение
        break #break - функция, прерывающая цикл

#Pyth4 4.9
#Посчитайте, сколько значений в словаре my_dict являются числами
my_dict = {'a': 15, 'b': 10.5, 'c': '15', 'd': 50, 'e': 15, 'f': '15'}
count = 0
for i in my_dict:
    if type(my_dict[i]) == str:
        continue
    else:
        count += 1
print(count)


#Pyth4 example 4
#Подсчитать количество вхождений каждого символа в заданном тексте
text = """
The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she found herself falling down a very deep well.
Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her and to wonder what was going to happen next. First, she tried to look down and make out what she was coming to, but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves; here and there she saw maps and pictures hung upon pegs. She took down a jar from one of the shelves as she passed; it was labelled `ORANGE MARMALADE', but to her great disappointment it was empty: she did not like to drop the jar for fear of killing somebody, so managed to put it into one of the cupboards as she fell past it.
`Well!' thought Alice to herself, `after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!' (Which was very likely true.)
"""
text = text.lower() #приводим текст к нижнему регистру
text = text.replace(" ", "") #заменяем пробелы на пустые строки
text = text.replace("\n", "") #заменяем символы переноса строки на пустые строки
count_dict = {} #создаём пустой словарь для подсчёта количества символов
#создаём цикл по символам в строке text
for symbol in text: #symbol — текущий символ в тексте
    #проверяем условие, что символа ещё нет среди ключей словаря
    if symbol not in count_dict: #если условие выполняется,
        count_dict[symbol] = 1 #заносим символ в словарь со значением 1
    else: #в противном случае
        count_dict[symbol] += 1 #увеличиваем частоту символа
print(count_dict) #выводим результирующий словарь

#Pyth4 example 5
#Подсчитать количество вхождений каждого слова в заданном тексте
text = """
She sells sea shells on the sea shore;
The shells that she sells are sea shells I am sure.
So if she sells sea shells on the sea shore,
I am sure that the shells are sea shore shells.
"""
text = text.lower() #приводим текст к нижнему регистру
text = text.replace("\n", " ") #заменяем символы переноса строки на пробелы
text = text.replace(",", "") #заменяем запятые на пустые строки
text = text.replace(".", "") #заменяем точки на пустые строки
text = text.replace(";", "") #заменяем точки с запятыми на пустые строки
word_list = text.split()
count_dict = {} #создаём пустой словарь для подсчёта количества слов
#создаём цикл по словам в списке word_list
for word in word_list: #word — текущее слово из списка word_list
    #проверяем условие, что слова ещё нет среди ключей словаря
    if word not in count_dict: #если условие выполняется,
        count_dict[word] = 1 #заносим слово в словарь со значением 1
    else: #в противном случае
        count_dict[word] += 1 #увеличиваем частоту слова
print(count_dict) #выводим результирующий словарь 

#Pyth4 5.1
#cоздаем список из 10 рандомных чисел
import random
my_list = []
for i in range(0, 10):
    my_list.append(random.randint(0, 10))
#С помощью цикла for проверьте, есть ли в полученном списке повторяющиеся числа. 
#Если хотя бы один из элементов встречается больше одного раза, выведите на экран строку 'yes' и прекратите выполнение цикла.
for i in my_list:
    if my_list.count(i) > 1:
        print('Yes')
        print(my_list)
        break
    
#Pyth4 5.2
#cоздаем список из 10 рандомных чисел
import random
my_list = []
for i in range(0, 10):
    my_list.append(random.randint(0, 10))
#Используя инструкцию while, разработайте программу, которая вычисляет сумму элементов списка, пока она не будет больше или равна 10.
sum_ = 0
i = 0
#print(my_list)
while sum_ < 10:
    sum_ += my_list[i]
    i += 1
    #print(my_list[i])
print('sum',sum_)

#Pyth4 5.3
#Вы играете в компьютерную игру, дошли до схватки с финальным боссом, но вот незадача: ваш компьютер «заглючил», и вы не можете управлять вашим персонажем. 
#Босс атакует и каждую секунду наносит один удар, который отнимает у персонажа 80 единиц здоровья. 
#На схватку с боссом ваш персонаж вышел с 500 единицами здоровья.
current_health = 500 #заданный показатель здоровья
attack = 80 #заданная атака босса
seconds_num = 0 #задаем начальное время схватки
for i in list(range(0, current_health, attack)):
    seconds_num += 1
print(seconds_num)

#Pyth4 5.4
# В цикле добавляйте в список cut_str_list списки, состоящие из порядкового номера строки из списка str_list (номер в рамках данной задачи начинается от 0) и 3 первых символа из каждой строки.
# Если длина строки меньше Трёх символов, то добавляется вся строка целиком.
# В результате работы вашей программы в переменной cut_str_list должен храниться результирующий вложенный список.

str_list = ["Hello", "my", "name", "is", "Ezeikel", "I", "like", "knitting"] #заданный список
cut_str_list = [] #задаем новый список

for i, g in enumerate(str_list):
    cut_str_list.append([i,g[:3]])
print(cut_str_list)

#Pyth4 5.5
#Выполните следующие действия:
#1. Приведите все символы в предложении к нижнему регистру.
#2. Исключите знаки препинания (запятые)
#3. Разделите строку по пробелам и создайте список слов, которые входят в предложение.
#4. Подсчитайте количество повторений каждого слова. 
#Для подсчёта слов используйте словарь word_dict. Ключами словаря будут являться слова, а значениями — число вхождений этих слов в предложение.
#В результате работы вашей программы в переменной word_dict должен храниться результирующий словарь.

sentence = "A roboT MAY Not injure a humAn BEING or, tHROugh INACtion, allow a human BEING to come to harm" #заданное предложение
word_dict = {} #создаем словарь для посчета количества слов

sentence = sentence.lower() #приводим текст к нижнему регистру
sentence = sentence.replace(",", "") #заменяем запятые на пустые строки
sentence_list = sentence.split()

for word in sentence_list:
    if word not in word_dict:
        word_dict[word] = 1 #заносим слово в словарь со значением 1
    else:
        word_dict[word] +=1 #увеличиваем частоту слова
print(word_dict)

#Pyth4 5.6
#Подсчитайте количество вхождений символа 't' в каждую из строк этого списка.
#Для подсчёта используйте словарь word_dict: в качестве ключа запишите в него строку, в качестве значения — число вхождений буквы 't' в эту строку.
#В результате работы вашей программы в переменной word_dict должен храниться результирующий словарь.

str_list = ["text", "morning", "notepad", "television", "ornament"] #заданный список слов
symbol_to_check = "t" #задаём символ, который будем искать
words_dict = {} #задаём пустой словарь для подсчёта

for i in str_list:
    words_dict.update({i: i.count('t')})
print(words_dict)

#Pyth4 Vebin
#Игра в орел/решку
import random #модуль для случайного отобора и генерации случайных чисел
print(random.choice['head', 'tail']) #choice - функция для задания выборки

#вывести для заданного количества персон рецепт с необходимым кол. ингредиентов
#знаем для 1-й персоны

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',  
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],  
      ]
  ]
]

person = 5

for dish, ingrs in cook_book: #распаковка - dish: блюдо, ingrs: ингредиенты
    print(f'{dish.capitalize()}:') #capitalize - первый символ строки с заглавной буквы
    # print(ingrs)
    for name, q, measure in ingrs: #распаковка ингредиентов на название, количество, единицу измерения
        print(f'{name} {q*person}{measure}') #печать через f строку с умножением кол. на кол. персон
    print()

#Pyth5.1 3.5
def add_mark(name, mark, journal=None):
   # Добавьте здесь проверку аргумента mark
    if mark in {2, 3, 4, 5}:
        pass
    else:
        raise ValueError("Invalid Mark!")
    if journal is None:
        journal = {}
    journal[name] = mark
    return journal

#попытка вызвать функцию с некорректными аргументами
try:
    print(add_mark('Ivanov', 6))
#должна завершиться с ошибкой ValueError, которую мы выведем в блоке except
except ValueError as e:
    print(e)


#Pyth5.1 5.2
#Напечатайте список langs с использованием * через запятую с пробелом.
langs = ['Python', 'SQL', 'Machine Learning', 'Statistics']
print(*langs, sep = ', ')

#Pyth5.1 5.3
#Передайте в функцию mean_mark этот список, а также фамилию студента Kuznetsov с помощью оператора распаковки.
marks = [4,5,5,5,5,3,4,4,5,4,5]
def mean_mark(name, *marks):
    result = sum(marks) / len(marks)
    # Не возвращаем результат, а печатаем его
    print(name+':', result)
mean_mark('Kuznetsov', *marks)

#Pyth5.1 6.1
#В качестве упражнения попробуйте переписать использованную lambda-функцию в классический вид (с def). Назовите её get_length.
new_list = ['bbb', 'ababa','aaa', 'aaaaa',  'cc']
def get_length(line):
    return len(line)
new_list.sort(key=get_length)
print(new_list)

#Pyth5.1 6.3
#Напишите lambda-функцию для расчёта гипотенузы прямоугольного треугольника
hyp = lambda a, b: (a**2 + b**2) ** (1/2)
print(hyp(3,4))


#Pyth5.1 6.4
#Напишите функцию sort_sides, которая сортирует переданный в неё список.
#Входной список состоит из кортежей с парами чисел — длинами катетов прямоугольных треугольников.
#Функция должна возвращать список, отсортированный по возрастанию длин гипотенуз треугольников.
def sort_sides(l_in):
    l_in.sort(key=lambda x: (x[0]**2 + x[1]**2) ** (1/2))
    return l_in
print(sort_sides([(3,4), (1,2), (10,10)]))


#Pyth5.1 7.9
#Напишите функцию get_less, которая принимает на вход через запятую список, состоящий из чисел, и ещё одно число. 
#Функция должна вернуть первое найденное число из списка, которое меньше переданного во втором аргументе. 
#Если такого числа нет, необходимо вернуть None.
def get_less(list_in, num):
    for i in list_in:
        if i < num:
            return i
    return None

#Pyth5.1 7.10
#Напишите функцию split_date(date), которая принимает на вход строку, задающую дату, в формате ддммгггг без разделителей. 
#Функция должна вернуть кортеж из чисел (int): день, месяц, год.
def split_date(date):
    days, months, years = int(date[:2]), int(date[2:4]), int(date[4:])
    return days, months, years


#Pyth5.1 7.11
#Напишите функцию is_prime(num), которая проверяет, является ли число простым.
#Функция должна вернуть True, если число простое, иначе — False.
def is_prime(num): #опеределяем через тест Люка
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

#Pyth5.1 7.12
#Напишите функцию between_min_max(...), которая принимает на вход числа через запятую.
#Функция возвращает среднее арифметическое между максимальным и минимальным значением этих чисел, то есть (max + min)/2.
def between_min_max(*nums):
    min_ = min(nums)
    max_ = max(nums)
    return (min_ + max_) / 2


#Pyth5.1 7.13
#Напишите функцию best_student(...), которая принимает на вход в виде именованных аргументов имена студентов и их номера в рейтинге (нагляднее в примере).
#Необходимо вернуть фамилию студента с минимальным номером по рейтингу.
def best_student(**stud):
    s_name = None
    s_rating = None
    for (student, rating) in stud.items():
        if s_name is None:
            s_name = student
            s_rating = rating
        if rating < s_rating:
            s_rating = rating
            s_name = student
    return s_name

#Pyth5.1 7.14
#Напишите lambda-функцию is_palindrom, которая принимает на вход одну строку и проверяет, является ли она палиндромом
is_palindrom = lambda x: 'yes' if x == x [::-1] else 'no'

#Pyth5.1 7.15
#Напишите lambda-функцию area, которая принимает на вход два числа — стороны прямоугольника — через запятую и возвращает площадь прямоугольника.
area = lambda x, y: x*y

#Pyth5.1 7.16
#Перепишите функцию between_min_max из задания 7.12 в lambda-функцию.
between_min_max = lambda *nums: (min(nums) + max(nums)) / 2

#Pyth5.1 7.17
#Напишите функцию sort_ignore_case, которая принимает на вход список и сортирует его без учёта регистра по алфавиту
def sort_ignore_case(ls):
    ls.sort(key = lambda x: x.lower())
    return ls

#Pyth5.1 7.18
#Напишите функцию exchange(usd, rub, rate), которая может принимать на вход сумму в долларах (usd), сумму в рублях (rub) и обменный курс (rate). 
#Обменный курс показывает, сколько стоит один доллар. Например, курс 85.46 означает, что один доллар стоит 85 рублей и 46 копеек.
#В функцию должно одновременно передавать два аргумента. Если передано менее двух аргументов, должна возникнуть ошибка ValueError('Not enough arguments'). 
#Если же передано три аргумента, должна возникнуть ошибка: ValueError('Too many arguments').
#Функция должна находить третий аргумент по двум переданным. 
def exchange(usd = None, rub = None, rate = None):
    err = [usd, rub, rate].count(None)
    err_lst = ['Too many arguments', None, 'Not enough arguments', 'Not enough arguments']
    if err != 1: 
        raise ValueError(err_lst[err])
    else:
        if usd is None:
            usd = rate / rub
            return usd
        if rub is None:
            rub = usd * rate
            return rub
        if rate is None:
            rate = rub / usd
            return rate

#Pyth5.2 2.5
#Напишите функцию-копилку с названием saver(), которая не принимает никаких аргументов. 
#Она должна возвращать внутреннюю функцию adder(), которая принимает на вход одно число и возвращает сумму в копилке после прибавления числа.
#Изначально в новой копилке хранится 0.
def saver():
    # Вместо pass напишите тело функции
    y = 0
    def adder(x):
        nonlocal y
        y += x
        return y
    return adder
pig = saver()
    
# print(pig(2))
# print(pig(6))


#Pyth5.2 3.4
#Напишите рекурсивную функцию multiply_lst(), которая перемножает элементы заданного списка между собой. 
def multiply_lst(lst):
    print(lst)
    if len(lst) == 0:
        return 1
    return lst[0] * multiply_lst(lst[1:])

my_lst = [10, 21, 24, 12]
print(multiply_lst(my_lst))


#Pyth 5.3 3.7
#Напишите рекурсивную функцию fib(n), которая считает n-ое число Фибоначчи. 
#Будем считать, что fib(0) = 0 и fib(1) = 1.
def fib(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(6))

#Pyth 5.3 4.5
#Напишите рекурсивную функцию power(val, n), которая возводит число в заданную целую натуральную степень (или в степень 0)
def power(val, n):
    # Вместо pass напишите тело функции
    if n == 0: return 1
    if n == 1: return val
    return val * power(val, n-1)
print(power(2, 3))


#Pyth 5.3 4.6
#Напишите функцию is_leap(year), которая принимает на вход год и возвращает True, если год високосный, иначе — False.
def is_leap(year):
    if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
        return True
    else:
        return False

#Pyth 5.3 4.7
#Напишите функцию check_date(day, month, year), которая проверяет корректность даты рождения
def check_date(day, month, year):
    #Все аргументы должны быть целыми числами (проверить с помощью type(day) is int)
    if (type(day) is not int) or (type(month) is not int) or (type(year) is not int):
        return False
    #Годом рождения не может быть год до 1900 и год после 2022
    if (year <= 1900) or (year >= 2022):
        return False
    #Номер месяца не может быть больше 12 и меньше 1     
    if (month > 12) or (month < 1):
        return False
    #Номер дня не может быть больше 31 и меньше 1  
    if (day < 1) or (day > 31): 
        return False
    #В сентябре, апреле, июне и ноябре 30 дней
    if (month in [4,6,9,11]) and (day > 30):
        return False
    #Если год является високосным, то в феврале (второй месяц) должно быть 29 дней, в противном случае — 28
    def is_leap(year):
        if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
            return True
        else:
            return False
    if month == 2:
        if (is_leap(year) and ((day < 1) or (day > 29))) or ((is_leap(year) == False) and 
        ((day < 1) or (day > 28))):
            return False
    return True


#Pyth 5.3 4.8
#регистрация пользователя
def check_date(day, month, year):
#Все аргументы должны быть целыми числами (проверить с помощью type(day) is int)
    if (type(day) is not int) or (type(month) is not int) or (type(year) is not int):
        return False
    #Годом рождения не может быть год до 1900 и год после 2022
    if (year <= 1900) or (year >= 2022):
        return False
    #Номер месяца не может быть больше 12 и меньше 1     
    if (month > 12) or (month < 1):
        return False
    #Номер дня не может быть больше 31 и меньше 1  
    if (day < 1) or (day > 31): 
        return False
    #В сентябре, апреле, июне и ноябре 30 дней
    if (month in [4,6,9,11]) and (day > 30):
        return False
    #Если год является високосным, то в феврале (второй месяц) должно быть 29 дней, в противном случае — 28
    def is_leap(year):
        if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
            return True
        else:
            return False
    if month == 2:
        if (is_leap(year) and ((day < 1) or (day > 29))) or ((is_leap(year) == False) and 
        ((day < 1) or (day > 28))):
            return False
    return True

def register(surname, name, date, middle_name = None, registry = None):
    if registry is None:
        registry = list()
    if not check_date(*date):
        raise ValueError("Invalid Date!")
    registry.append((surname, name, middle_name, date[0], date[1], date[2]))
    return registry


#Pyth 5.3 5.7
#Напишите бесконечный итератор по списку.
#Для этого создайте генератор с названием inf_iter, который принимает на вход список и возвращает элементы из него через yield.
#Когда элементы в списке заканчиваются, генератор снова возвращает элементы из списка, начиная с нулевого.
#В теле генератора организуйте бесконечный цикл (внутри бесконечного цикла реализуется цикл  for). 
#В цикле for пройдитесь по списку и выдавайте его элементы с помощью yield. 
#Так вы получите циклический доступ к элементам списка.
def inf_iter(l_in):
    while True:
        for i in iter(l_in):
            yield i
#l_in = [101, 102, 103]
# gen = inf_iter(l_in)
# for _ in range(10):
#     print(next(gen))


#Pyth 5.3 5.8
#Напишите генератор group_gen(n). 
#Он должен при каждом вызове выдавать порядковый номер от 1 до n (включая n). 
#После достижения n генератор должен снова возвращать номера, начиная с 1.
def group_gen(n):
    while True:
        for i in range(n):
            yield i + 1
# groups = group_gen(3)
# for _ in range(10):
#     print(next(groups))

#Сокращенная запись генераторов
#Например, посчитаем кубы первых 15 натуральных чисел, которые делятся на 3
# Создаём генератор кубов чисел, которые делятся на 3
triple_cubes_generator = (x**3 for x in range(1,16) if x % 3 == 0)
print(type(triple_cubes_generator))
# Оборачиваем сгенерированные значения в список
print(list(triple_cubes_generator))
# Будет напечатано:
# <class 'generator'>
# [27, 216, 729, 1728, 3375]


#Pyth 5.3 6.1
#Cоставить новый список links, в котором будут храниться полные ссылки до статей на сайте Коммерсант.
main_link = 'https://www.kommersant.ru'
docs = [
    '//doc/5041434?query=data%20science',
    '//doc/5041567?query=data%20science',
    '//doc/4283670?query=data%20science',
    '//doc/3712659?query=data%20science',
    '//doc/4997267?query=data%20science',
    '//doc/4372673?query=data%20science',
    '//doc/3779060?query=data%20science',
    '//doc/3495410?query=data%20science',
    '//doc/4308832?query=data%20science',
    '//doc/4079881?query=data%20science'
]

links = list(map(lambda x: main_link + x, docs))
print(links)

#Pyth 5.3 6.2
#Необходимо написать функционал, который позволяет отфильтровать среди всех запрашиваемых пользователем услуг (их количество произвольное) только те, которые предоставляются многодетным семьям.
def family(*full_list):
    family_list = [
    'certificate of a large family',
    'social card',
    'maternity capital',
    'parking permit',
    'tax benefit',
    'reimbursement of expenses',
    "compensation for the purchase of children's goods"
    ]
    return list(filter(lambda x: x in family_list, full_list))

print(family(
    'newborn registration',
    'parking permit',
    'maternity capital',
    'tax benefit',
    'medical policy'
    )
)


#Pyth 5.3 6.3
#Выберите из списка reg только те записи, в которых год рождения пользователя 2000 и больше (2001, 2002 и т. д.). 
#Из оставшихся записей составьте новый список кортежей
#Фамилия и имя объединены в одну строку по следующему шаблону Фамилия И.
reg = [('Ivanov', 'Sergej', 24, 9, 1995),
      ('Smith', 'John', 13, 2, 2003),
      ('Petrova', 'Maria', 13, 3, 2003)]

#ваш код здесь
reg_1 = filter(lambda x: x[4] >= 2000, reg)
new_reg = list(map(lambda x: (x[0] + " " + x[1][0] + '.', x[2], x[3], x[4]) ,reg_1))
print(new_reg)


#Pyth 5.3 6.4
#Напишите функцию print_groups, которая принимает список с именами пользователей. 
#Используя генератор групп group_gen, печатайте на экран:
#<Фамилия И.> in group <номер группы по порядку>.
def group_gen(n=3):
    while True:
        for i in range(1, n+1):
            yield i


def print_groups(users):
    for group, user in zip(group_gen(), users):
        print(user, 'in group', group)
        
users = ['Smith J.', 'Petrova M.', 'Lubimov M.', 'Holov J.']
print_groups(users)


#Pyth 5.3 7.3
#Напишите функцию-декоратор-логгер logger(name).
#При создании декоратора передаётся имя логгера, которое выводится при каждом запуске декорируемой функции.
#Декорированная функция должна печатать:
#перед запуском основной:
#<имя логгера>: Function <имя декорируемой функции> started
#после запуска основной:
#<имя логгера>: Function <имя декорируемой функции> finished
def logger(name):
    def decorator(func):
        def dec_func (*args, **kwargs):
            print (name +':',  'Function',  func.__name__, 'started')
            result = func(*args, **kwargs)
            print (name +':',  'Function',  func.__name__, 'finished')
            return result
        return dec_func
    return decorator


#Pyth 6 1.5
#Посчитайте количество символов в следующей строке:
python_string = 'Hello! My name is Python. I will help you to analyze some data'
print(len(python_string) ** 3)

#Pyth 6 1.6
#С помощью среза выведите на экран слово Python из строки в задании 1.5
print(python_string[18:24])

#Pyth 6 1.7
#Возьмите строку python_string из задания 1.5, избавьтесь от знаков препинания в ней. 
#Посчитайте количество слов в строке и запишите это число в ответ.
python_string = python_string.replace(",", "")
python_string = python_string.replace("!", "")
python_string = python_string.replace(".", "")
word_list = python_string.split()
print(len(word_list))


#Pyth 6 1.8
#Напишите функцию change_password, которая должна возвращать отформатированную строку в следующем виде:
#User user_name changed password to new_password
def change_password(user_name, new_password):
    return 'User {} changed password to {}'.format(user_name, new_password)

print(change_password("Lena", "qwerty"))


#Pyth 6 2.5
#Напишите функцию get_unique_words(), которая избавляется от знаков препинания в тексте и возвращает упорядоченный список (слова расположены по алфавиту) из уникальных (неповторяющихся) слов. 
#Учтите, что слова, написанные в разных регистрах считаются одним и тем же словом.
punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

def get_unique_words(text):
    for i in punctuation_list:
        text = text.replace(i, ' ')
    text = text.lower()
    text_lst = text.split()
    text_lst = list(set(text_lst))
    text_lst.sort()
    return text_lst
print(get_unique_words(text_example))


#Pyth 6 2.6
#Необходимо написать функцию get_most_frequent_word(), которая возвращает самое часто встречающееся слово в тексте. 
#Не забудьте очистить тест от знаков пунктуации и привести текст к единому регистру (слова в верхнем и нижнем регистре считаются одним и тем же словом).
punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

def get_most_frequent_word(text):
    for i in punctuation_list:
        text = text.replace(i, "")
    text = text.lower()
    text_lst = text.split()
    unique_words = list(set(text_lst))
    unique_words.sort()
    w_count = 0
    most_frequent_word = ''
    for word in unique_words:
        if text_lst.count(word) > w_count:
            w_count = text_lst.count(word)
            most_frequent_word = word
    return most_frequent_word

print(get_most_frequent_word(text_example))


#Pyth 6 2.7
#Разработайте функцию holes_count(), которая подсчитывает количество отверстий в заданном числе. Например, в цифре 8 два отверстия, в цифре 9 — одно. 
#В числе 146 два отверстия.
def holes_count(number):
    numder_hole = {'0': 1, '1': 0, '2': 0, '3': 0, '4': 1, '5': 0, '6': 1, '7': 0, '8': 2, '9': 1}
    hole_count = 0
    number = str(number)
    for i in number:
        hole_count += numder_hole[i]
    return hole_count

print(holes_count(123))
print(holes_count(8888))


#Pyth 6 2.8
#Напишите программу, которая запрашивает у пользователя следующие данные : 
#username, age, email о нескольких пользователях и собирает эти данные в структуру:
#[(1, {'username': user1, 'age': age1, 'email': email1}), (2, {'username': user2, 'age': age2, 'email': email2}), ... ]
#Первый элемент каждого кортежа — порядковый номер пользователя, второй элемент — словарь с данными.
#Далее необходимо провести аналитику (собрать данные о пользователях в словарь):
#{'username': [user1, user2, ...], 'age': [age1, age2, ...], 'email': [email1, email2, ...]}
#и вывести эту аналитику на экран.
num_users = int(input('Enter number of users: '))
user_analytics = {'username': [], 'age': [], 'email': []}
user_list = []

for i in range(num_users):
    user = {}
    user['username'] = input("Enter username: ")
    user['age'] = int(input("Enter user age: "))
    user['email'] = input("Enter user email: ")
    user_analytics['username'].append(user['username'])
    user_analytics['age'].append(user['age'])
    user_analytics['email'].append(user['email'])
    user_list.append((i + 1, user))

print(user_list)
print(user_analytics)


#Pyth 6 3.4
#Напишите функцию find_min_number(), которая принимает три числа на вход и возвращает наименьшее из них
#через min
def find_min_number(a, b, c):
  return min(a, b ,c)

print(find_min_number(1, 2, 3))
#через условия
def find_min_number(a, b, c):
    min_number = 0
    if a < b:
        min_number = a
    else:
        min_number = b
    if min_number > c:
        min_number = c
    return min_number

print(find_min_number(1, 2, 3))


#Pyth 6 3.5
#Напишите функцию sum_min_numbers(), которая также принимает на вход три числа и возвращает сумму двух наименьших
def find_min_number(a, b, c):
    min_number = 0
    if a < b:
        min_number = a
    else:
        min_number = b
    if min_number > c:
        min_number = c
    return min_number
  
def sum_min_numbers(a, b, c):
    min_number = find_min_number(a, b, c)
    number_list = [a, b, c]
    number_list.remove(min_number)
    if number_list[0] < number_list[1]:
        sum_min = min_number + number_list[0]
    else:
        sum_min = min_number + number_list[1]
    return sum_min

print(sum_min_numbers(1, 2, 3))


#Pyth 6 3.6
# Напишите функцию is_divided_by_six(), которая проверяет, делится ли число на шесть. 
# При решении воспользуйтесь тернарным оператором!
# Функция должна вернуть True, если число делится на шесть или False в обратном случае.

def is_divided_by_six(number):
  return True if (number % 3 == 0) and (number % 2 == 0) else False

print(is_divided_by_six(13))
print(is_divided_by_six(12))



#Pyth 6 3.7
# Напишите функцию check_number_sign(), которая возвращает 1, если число положительное, 
# -1, если число отрицательное, 0, если число - 0.
# Используйте в коде конструкцию if-elif-else.
# Функция принимает на вход одно число.

def check_number_sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


print(check_number_sign(0))
print(check_number_sign(100))
print(check_number_sign(-1))


#Pyth 6 3.8
# Напишите функцию def division(), которая осуществляет деление двух чисел. 
# Необходимо реализовать внутри функции отлов исключения ZeroDivisionError, 
# в случае, если пользователь, при вызове функции, пытается поделить на ноль.
# Функция принимает на вход два числа - делимое и делитель.

def division(a, b):
    try:
        div_ = a / b
    except ZeroDivisionError:
        print('Error! Matrices dimensions are different!')
        return
    return div_

print(division(1, 0))
print(division(1, 1))


#Pyth 6 4.4
# Напишите функцию lucky_ticket(), которая проверяет, является ли билетик счастливым.
# Памятка: билетик счастливый, если сумма первых трех цифр равна сумме последних трех цифр.
# На вход функция получает шестизначное число.

def lucky_ticket(ticket_number):
    number_list = list(str(ticket_number))
    #print(number_list)
    #print(number_list[:3])
    #print(number_list[-3:])
    sum_1 = 0
    sum_2 = 0
    for i in number_list[:3]:
        sum_1 += int(i)
    for i in number_list[-3:]:
        sum_2 += int(i)
    if sum_1 == sum_2:
        return True
    else:
        return False

print(lucky_ticket(111111))
print(lucky_ticket(123456))


#Pyth 6 4.5
# Напишите функцию def fib_number(), которая получается на вход некоторое 
# число n и выводит n-e число Фибоначчи. 
# Задачу можно решить как с помощью цикла for, так и с помощью цикла while
# десь необходимо реализовать те же вычисления, но без использования рекурсии.

def fib_number(n):
    fib = 0
    a0 = 0
    a1 = 1
    if n == 0:
        return a0
    elif n == 1:
        return a1
    else:
        for i in range(n - 1):
            fib = a0 + a1
            a0 = a1
            a1 = fib
        return fib

print(fib_number(0))
print(fib_number(1))
print(fib_number(2))


#Pyth 6 4.6
# Напишите функцию def even_numbers_in_matrix(), 
# которая получает на вход матрицу (список из списков) 
# и возвращает количество четных чисел в ней.

matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]

def even_numbers_in_matrix(matrix):
    count = 0
    for i in range(len(matrix)):
        for g in range(len(matrix[i])):
            if matrix[i][g] % 2 == 0:
                count += 1
    return count

print(even_numbers_in_matrix(matrix_example))



#Pyth 6 4.7
# Напишите функцию def matrix_sum(), которая получает на вход две матрицы 
# и возвращает их сумму.

# Примечание: чтобы найти сумму двух матриц, нужно просуммировать 
# их соответствующие элементы. Но перед этим необходимо проверить, что размеры 
# матриц одинаковы (одинаковое количество столбцов и одинаковое количество строк)

# Например:

# 1 2 3   2 3 4   3 5 7
# 2 3 4 + 4 5 6 = 6 8 10
# 5 6 7   4 3 2   9 9 9

matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]

def matrix_sum(matrix1, matrix2):
    matrix_s = []
    eq_matrix = True
    
#Проверка длины строк
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            eq_matrix = False
            print('Error! Matrices dimensions are different!')
            return
        
#Проверка длины столбцов и возвращение None        
    if len(matrix1) != len(matrix2) or eq_matrix == False:
        print('Error! Matrices dimensions are different!')
        return

#Суммирование матриц    
    for i in range(len(matrix1)):
        matrix_temp = []
        for j in range(len(matrix1[i])):
            matrix_temp.append(matrix1[i][j] + matrix2[i][j])
        matrix_s.append(matrix_temp)
    return matrix_s

print(matrix_sum(matrix_example, matrix_example))


#Pyth 6 4.8
#Реализуйте программу, которая сжимает последовательность символов. 
#На вход подаётся последовательность вида:
#aaabbccccdaa
#Необходимо вывести строку, состоящую из символов и количества повторений этого символа. 
#Вывод должен выглядеть как:
#a3b2c4d1a2
str_example = 'aaabbccccdaa'
first_symbol = str_example[0]
count = 0
new_str = ''
for symbol in str_example:
    if symbol == first_symbol:
        count += 1
    else:
        new_str += first_symbol + str(count)
        first_symbol = symbol
        count = 1

new_str += first_symbol + str(count)
print(new_str)


