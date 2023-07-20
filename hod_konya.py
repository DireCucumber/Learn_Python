# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли конь попасть с первой клетки на вторую одним ходом. 
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
# Программа должна вывести «YES», если из первой клетки ходом коня можно попасть во вторую или «NO» в противном случае.

# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# put your python code here
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
    print("YES")
else:
    print("NO")