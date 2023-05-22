# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)
import random
n = int(input("Введите длинну первой строки "))
lst = [random.randint(0, 12) for i in range(n)]
minn = int(input("Введите минимум "))
maxn = int(input("Введите максимум "))
print (lst)
for i in range(len(lst)):
    if minn <= lst[i] <= maxn:
        print(i)

