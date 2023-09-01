from random import randint

bushQty_list = list(randint(1, 21) for i in range(int(input('Введите кол-во кустов: '))))
print(bushQty_list)

a = int(input('Введите № куста: '))
res = 0

if a == 1:
    res = bushQty_list[0] + bushQty_list[1] + bushQty_list[-1]
elif a == len(bushQty_list):
    res = bushQty_list[-2] + bushQty_list[-1] + bushQty_list[0]
else:
    res = bushQty_list[a-1] + bushQty_list[a-2] + bushQty_list[a]
    
print(res, 'ягод')