# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
# Возьмем за x количество журавликов, которые сделал Петя.
# Сережа сделал столько же журавликов, что и Петя. Катя сделала в два раза больше,
#  чем они вместе взятые.
# Получается уравнение 6x = s

s = int(input("Сколько всего журавликов сделали детки? "))
print("По", s/6, "журавликов сделали Петя и Сережа")
print((s/6)*4, "журавликов сделала Катя")
