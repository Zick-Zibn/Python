qty = int(input('Введите количество монет '))
side1 = 0
side2 = 0

for i in range(qty):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        side1 += 1
    else:
        side2 += 1

if side1 < side2:
    print(f'Переверните {side1} монет с орла на решку, их меньше всего')
elif side1 == side2:
    print(f'Количество орлов и решек одинаково, по {side1} штук')
else:
    print((f'Переверните {side2} монет с решки на орла, их меньше всего'))            