###############################
### |ДЗ 27.05.2023 СЕМИНАР| ###
###############################
# ПОДКЛЮЧАЕМЫЕ БИБЛИОТЕКИ:
import random # подключение библиотеки для функционирования random.randint(0, 10)
#####################################################
"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    3
    -> 1
"""

# count = 0
# list_1 = [random.randint(0, 10) for i in range(int(input("Укажите размер массива: ")))]
# x = int(input("Укажите число от 1 до 10, что бы узнать сколько раз оно встретится в массиве: ")) 
# print(list_1)

# for i in list_1:
#     if i == x:
#         count +=1
# print("Число {} встречается в массиве {} раз.".format(x, count))

#####################################################

#####################################################
"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""

# list_1 = [random.randint(0, 10) for i in range(int(input("Укажите размер массива: ")))]
# x = int(input("Укажите число от 1 до 10, что бы узнать самый близкий по величине элемент к нему: ")) 
# print(list_1)
# result = 0
# max = list_1[0] 
# flag = False

# for m in range(len(list_1)): 
#   if list_1[m] > max:
#     max = list_1[m]

# for j in range(x+max): 
#   for i in list_1: 
#     if flag == False:
#         if i == x:
#             result = i
#             flag = True
#         elif (j+i == x or j-i == x):
#             result = i
#             flag = True
# print(result)


# # КОД С КОММЕНТАРИЯМИ
# list_1 = [random.randint(0, 10) for i in range(int(input("Укажите размер массива: ")))]
# x = int(input("Укажите число от 1 до 10, что бы узнать самый близкий по величине элемент к нему: ")) 
# print(list_1)
# result = 0
# max = list_1[0] # Поиска Макса необходим, если искомое значение меньше элементов указанных в массиве
# flag = False

# # Поиска Макса НАЧАЛО
# for m in range(len(list_1)): 
#   # print(f"m={m}") # ВСПОМОГАТЕЛЬНЫЙ ПОКАЗ ЗНАЧЕНИЙ ДЛЯ ОТЛАДКИ КОДА (МОЖНО УДАЛИТЬ!)
#   if list_1[m] > max:
#     max = list_1[m]
#     # print(f"max={max}") # ВСПОМОГАТЕЛЬНЫЙ ПОКАЗ ЗНАЧЕНИЙ ДЛЯ ОТЛАДКИ КОДА (МОЖНО УДАЛИТЬ!)
# # КОНЕЦ

# for j in range(x+max): # Подбираем минимальное отклонение при котором один из элемент массива будет самым близким по величине к заданному числу X.
#   for i in list_1: # Перебираем элементы массива
#     # print(f"j={j} i={i}") # ВСПОМОГАТЕЛЬНЫЙ ПОКАЗ ЗНАЧЕНИЙ ДЛЯ ОТЛАДКИ КОДА (МОЖНО УДАЛИТЬ!)
#     if flag == False:
#         # print(f"result={result} != x={x}")  # ВСПОМОГАТЕЛЬНЫЙ ПОКАЗ ЗНАЧЕНИЙ ДЛЯ ОТЛАДКИ КОДА (МОЖНО УДАЛИТЬ!)
#         if i == x:
#             # print(f"1-Finish!!! {result}")  # ВСПОМОГАТЕЛЬНЫЙ ПОКАЗ ЗНАЧЕНИЙ ДЛЯ ОТЛАДКИ КОДА (МОЖНО УДАЛИТЬ!)
#             result = i
#             flag = True
#         elif (j+i == x or j-i == x):
#             # print(f"j{j}+i{i} = {j+i} | j({j})-i({i}) = {j-i}")  # ВСПОМОГАТЕЛЬНЫЙ ПОКАЗ ЗНАЧЕНИЙ ДЛЯ ОТЛАДКИ КОДА (МОЖНО УДАЛИТЬ!)
#             result = i
#             # print(f"2-Finish!!! {result}") # ВСПОМОГАТЕЛЬНЫЙ ПОКАЗ ЗНАЧЕНИЙ ДЛЯ ОТЛАДКИ КОДА (МОЖНО УДАЛИТЬ!)
#             flag = True
#     # else: # ВСПОМОГАТЕЛЬНЫЙ ПОКАЗ ЗНАЧЕНИЙ ДЛЯ ОТЛАДКИ КОДА (МОЖНО УДАЛИТЬ!)
#       # print(f"3-Finish!!! {result}") # ВСПОМОГАТЕЛЬНЫЙ ПОКАЗ ЗНАЧЕНИЙ ДЛЯ ОТЛАДКИ КОДА (МОЖНО УДАЛИТЬ!)
# print(result)

#####################################################

#####################################################
"""
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
либо только русские буквы.
*Пример:*
ноутбук
    12
"""
# # price_english_letters - стоимость английских букв:
# price_english_letter_1 = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1)
# price_english_letter_2 = dict.fromkeys(['D', 'G'], 2)
# price_english_letter_3 = dict.fromkeys(['B', 'C', 'M', 'P'], 3)
# price_english_letter_4 = dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4)
# price_english_letter_5 = dict.fromkeys(['K'], 5)
# price_english_letter_6 = dict.fromkeys(['J', 'X'], 8)
# price_english_letter_7 = dict.fromkeys(['Q', 'Z'], 10)
# # price_russian_letters - стоимость русских букв:
# price_russian_letters_1 = dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
# price_russian_letters_2 = dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2)
# price_russian_letters_3 = dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3)
# price_russian_letters_4 = dict.fromkeys(['Й', 'Ы'], 4)
# price_russian_letters_5 = dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
# price_russian_letters_6 = dict.fromkeys(['Ш', 'Э', 'Ю'], 8)
# price_russian_letters_7 = dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)
# # Словарь словарей english | russian буквами:
# dict_price = price_english_letter_1 | price_english_letter_2 | price_english_letter_3 | price_english_letter_4 | price_english_letter_5 | price_english_letter_6 | price_english_letter_7 | price_russian_letters_1 | price_russian_letters_2 | price_russian_letters_3 | price_russian_letters_4 | price_russian_letters_5 | price_russian_letters_6 | price_russian_letters_7

# user_word = input("Введите слово, что бы узнать его стоимость: ").upper()
# user_points = 0

# for i in user_word:
#     user_points += dict_price[i]
# print("Слово {} стоит {}".format(user_word, user_points)) 

#####################################################

#####################################################
"""
ПОШЛА В ДЗ
Задача №21. Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит
"""

# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# n = None
# s = set()
# for i in range(len(list_1)):
#   n = list_1.pop() # удаляем из списка последний словарь и помещаем его в переменную - n
#   for (k, v) in n.items(): # переводим  словарь в список из картежей функцией .items
#     s.add(v.replace(" ","")) # обращаемся к значению список по ключу V, удаляем лишние пробелы функцией .replace и добавляем получившееся значение в множество
# print(s) # Печатаем уникальное множество

#####################################################

#####################################################
"""
ПОШЛА В ДЗ
Задача №23. Дан массив, состоящий из целых чисел.
Напишите программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
Примечание: Пользователь может вводить значения
списка или список задан изначально.
"""
# count = 0
# j = 0 # шаг в перёд перед циклом
# list_1 = [0, -1, 5, 2, 3]

# for  i in range(len(list_1)):
    
#   if i == len(list_1)-1: # Костыль для предотвращения вываливания за пределы массива
#     j = i
#   else:
#     j = i+1 # шаг в перёд перед циклом

#   if list_1[i] < list_1[j]:
#     count += 1

# print(count)

#####################################################