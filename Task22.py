from random import randint
set_one = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(set_one)
set_two = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(set_two)
repeating_set = sorted(set_one.intersection(set_two))
print(*repeating_set)