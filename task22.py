import random
n = int(input("Введите длинну первой строки "))
lst = [random.randint(0, 12) for i in range(n)]
m = int(input("Введите длинну второй строки "))
lst2 = [random.randint(0, 12) for i in range(m)]
print(sorted(lst))
print(sorted(lst2))
lst3 =  set(lst).intersection(lst2)

print(sorted(lst3))