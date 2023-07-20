# Заданы две клетки шахматной доски. Напишите программу, которая определяет, имеют ли указанные клетки один цвет или нет. Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета, то «NO».

# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a + b + c + d) % 2 == 0:
    print("YES")
else:
    print("NO")