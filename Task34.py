def rhythm(str):

    str = str.split()
    list_Word = []

    for word in str:
        sum_w = 0

        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
                
        list_Word.append(sum_w)

    return len(list_Word) == list_Word.count(list_Word[0])

phrase = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

if rhythm(phrase):
    print('Парам пам-пам')
else:
    print('Пам парам')