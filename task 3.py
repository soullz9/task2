#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.]

number = int(input('Введите предел: '))
new_list = []
i = 0
while 2**i < number:
    new_list.append(2**i)
    i += 1

print(*new_list)