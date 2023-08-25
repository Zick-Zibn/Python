number = int(input('Введите число N '))
flag = False
degree = 2

for i in range(number):
    if flag == False:
        x = degree ** i
        if x <= number:
            print(x, end=' ')
            x = 2
        else:
            flag = True
    else:
        i = number