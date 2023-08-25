x = int(input('Введите первое натуральное число X от 1 до 1000 '))
y = int(input('Введите второе натуральное число Y от 1 до 1000 '))
if x < 1 or x > 1000 or y < 1 or y > 1000:
    print('Вы ввели число не из заданного диапазона!')
else:
    S = x + y
    P = x * y
    flag = False
    for i in range(1001):
        if flag == False:
            for j in range(1001):
                if flag == False:
                    if i * j == P and i + j == S:
                        print(i, j)
                        flag = True
            else:
                j = 1001
        else:
            i = 1001