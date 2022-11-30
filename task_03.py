# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму

n = int(input('input n: '))
list = []
for i in range(n):
    list.insert(i, round((1+1/(i+1))**(i+1), 3))
print(sum(list))