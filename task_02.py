#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('input N: '))

list = []
for i in range(n):
    count = 0
    res = 1
    for j in range(i+1):
        res = res * (count + 1)
        count+=1
    list.insert(i, res)
print(list)