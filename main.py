# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'
#
# print(',' .join([i for i in st if i.isdigit()]))
# #

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# st = 'as 23 fdfdg544 34'
#
# print(',' .join(''.join([i if i.isdigit() else '' for i in st]).split()))
#

# #################################################################################
#
# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# greeting = 'Hello, world'
#
# print([i.upper() for i in greeting])

#
# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([i**2 for i in range(50) if i % 2 != 0])
# function
#
# - створити функцію яка виводить ліст
# def func1(arr):
#     print(arr)
# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def min (a,b,c):
#     res = min(a,b,c)
#     print(res)
#     return res
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def max (a,b,c):
#     res = max(a,b,c)
#     print(res)
#     return res
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def min_max(*args):
#     print(args)
#     return min(args)
# - створити функцію яка повертає найбільше число з ліста
# def min_by_list(l):
#     return min(l)

# - створити функцію яка повертає найменьше число з ліста
# def max_by_list(l):
#     return min(l)
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def summator(l):
#     return sum(l)
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def avg(l):
#     return sum(l)/len(l)
#
#
#
#
#
#
#
# #################################################################################################
# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - найти min число в листе
#   - удалить все дубликаты в листе
#   - заменить каждое четвертое значение на "Х"
# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# 3) вывести табличку умножения с помощью цикла while
# 4) переделать первое задание под меню с помощью цикла


# l = [22, 3,5,2,8,2,-23, 8,23,5]
#
# print(min_by_list(l))
# # - найти min число в листе
# print(list(set(l)))
# #   - удалить все дубликаты в листе
#
# def duplicate(l):
#     print(list(set(l)))
# def func2(l):
#     for i in range(3, len(l), 4):
#         l[i] = 'x'
#     print(l)
#
# func2()
# print(l)
# #   - заменить каждое четвертое значение на "Х"
#
# while True:
#     l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     print('1) min ')
#     print('2) duplicate')
#     print ('3) x')
#     print('9) exit')
#     choise = input('make your choice: ')
#
#     if choice == '1':
#         min_by_list(l)
#     elif choise == '2':
#         duplicate(l)
#     elif choice == '3':
#         func2(l)
#     elif choice == '9':
#         break
#

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# def squere(n):
#     for i in range(n):
#         if i==0 or i == n-1:
#             print('*'*n)
#         else:
#         print('*'+''*(n-2)+'*')
#
# square(10)


# 3) вывести табличку умножения с помощью цикла while

# i = j = 1
#
# while i<10:
#     j=1
#     while j<10:
#         multi = i*j
#         print(multi, end='')
#         print(' ' if multi//10 else '   ', end='')
#         j += 1
#      i += 1
#     print()
print()