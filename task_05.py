# Реализуйте алгоритм перемешивания списка.

import random
list = [1,2,3,4,5,6,7,8]
res = []
print(list)
for i in range(len(list)):
    k = random.randint(0, len(list)-1)
    res.append(list[k])
    list.pop(k)
print(res)
