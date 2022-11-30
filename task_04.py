#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
n = int(input('input N: '))
list = []
res = 1
for i in range(n):
    list.append(randint(-n, n))
print(list)
pos = open('file.txt', 'r')
for j in pos:
    res = res * (list[int(j)])
print(res)
pos.close