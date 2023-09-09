from random import randint

list_1 = list(randint(-20, 21) for i in range(int(input('Введите размер списка: '))))
print (list_1)
list_2 = []
max = 10
min = 6
for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
        list_2.append(i)
print(list_2)

