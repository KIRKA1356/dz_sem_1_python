# 1-Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет
# 2-Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Должна получиться таблица истинности.

# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# 4- Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 5-Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


# #Задача 1
# def day_of_the_week():
#     number = int(input("Введите порядковый номер дня недели: "))
#     if number == 6 or number == 7:
#         print("Да")
#     elif number >= 8:
#         print("Нет такого дня недели")
#     else:
#         print("Нет")

# day_of_the_week()

# #Задача 2

# print("X          Y            Z        Result")
# print("--------------------------------")
# for x in (True, False):
#     for y in (True, False):
#         for z in (True, False):
#             if (not (x or y or z) == (not x and not y and not z)) == True:
#                 print(f'{x}       {y}        {z}       True')


# #Задача 3
# def number_of_quarter():
#     cordinate_x = int(input("Введите координату X: "))
#     cordinate_y = int(input("Введите координату Y: "))
#     if cordinate_x > 0 and cordinate_y > 0:
#         print("1я четверть")
#     elif cordinate_x < 0 and cordinate_y > 0:
#         print("2я четверть")
#     elif cordinate_x < 0 and cordinate_y < 0:
#         print("3я четверть")
#     elif cordinate_x > 0 and cordinate_y < 0:
#         print("4я четверть")
#     elif cordinate_x == 0 and cordinate_y < 0:
#         print("Точка лежит на плоскости Y, между 3ей и 4ой плоскостями")
#     elif cordinate_x == 0 and cordinate_y > 0:
#         print("Точка лежит на плоскости Y, между 1ой и 2ой плоскостями")
#     elif cordinate_x > 0 and cordinate_y == 0:
#         print("Точка лежит на плоскости X, между 1ой и 4ой плоскостями")
#     elif cordinate_x < 0 and cordinate_y == 0:
#         print("Точка лежит на плоскости X, между 2ой и 3ей плоскостями")

# number_of_quarter()

# #Задача 4

# def number_of_cordinate():
#     quarter_number = int(input("Введите номер четверти: "))
#     if quarter_number == 1:
#         print("X∈[0; ∞)    Y∈[0; ∞)")
#     elif quarter_number == 2:
#         print("X∈[0; -∞)    Y∈[0; ∞)")
#     elif quarter_number == 3:
#         print("X∈[0; -∞)    Y∈[0; -∞)")
#     elif quarter_number == 4:
#         print("X∈[0; ∞)    Y∈[0; -∞)")

# number_of_cordinate()

# # Задача 5

# def distance_between_points():
#     X_1 = int(input("Введите X координату 1ой точки: "))
#     Y_1 = int(input("Введите Y координату 1ой точки: "))
#     X_2 = int(input("Введите X координату 2ой точки: "))
#     Y_2 = int(input("Введите Y координату 2ой точки: "))
#     distance = round((((X_2 - X_1) ** 2 + (Y_2 - Y_1) ** 2) ** 0.5), 4)
#     print(f'Расстояние между точками равно: {distance}')


# distance_between_points()
