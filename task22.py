import random
n = int(input("Введите длинну первой строки "))
lst = [random.randint(0, 12) for i in range(n)]
m = int(input("Введите длинну второй строки "))
lst2 = [random.randint(0, 12) for i in range(m)]

lst3 = lst + lst2
lst3.sort()
print(lst)
print(lst2)
print(lst3)
print(set(lst3))