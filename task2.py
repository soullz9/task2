# Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

summa = int(input('Сумма чисел: '))
mult = int(input('Произведение чисел: '))

find = False
for i in range(1, 1000):
    if find:
        break
    for j in range(i, 1000):
        if i+j == summa and i*j == mult:
            find = True
            print(i, j)
            break