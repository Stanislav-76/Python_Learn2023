# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

n = int(input())
a = [int(input()) for i in range(n)]
x = int(input('Введите заданное число '))
res = 0
for i in a:
    if abs(x - i) < abs(x - res):
        res = i
print(res)