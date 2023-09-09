from random import randint

list_number = list(randint(-20, 21) for i in range(int(input('Введите размер списка: '))))
print (list_number)
list_min_max = []
max_number = int(input('Введите верхний диапазон: '))
min_number = int(input('Введите нижний диапазон: '))

for i in range(len(list_number)):
    if list_number[i] >= min_number and list_number[i] <= max_number:
        list_min_max.append(i)

print(list_min_max)

