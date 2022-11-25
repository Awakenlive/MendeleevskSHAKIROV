number = int(input())
number2 = number // 100
# Для тысячи
number3 = number - (number2 * 100)
# Для десятков
number4 = number3 // 10
# Отделил 3 число (--1-)
number5 = number3 - (number4 * 10)
# Отделил 4 число (---2)
number6 = number2 // 10
# Отделил 1 число (3---)
number7 = (number - (number6 * 1000 + number3)) // 100
# Отделил 2 число (-4--)
if number6 > number7 > number4 > number5:
    print(number5 * 1000 + number4 * 100 + number7 * 10 + number6)
# 4321
elif number7 > number6 > number4 > number5:
    print(number5 * 1000 + number4 * 100 + number6 * 10 + number7)
# 3421
elif number4 > number6 > number7 > number5:
    print(number5 * 1000 + number7 * 100 + number6 * 10 + number4)
# 3241
elif number5 > number6 > number7 > number4:
    print(number4 * 1000 + number7 * 100 + number6 * 10 + number5)
# 3214
elif number4 > number7 > number5 > number6:
    print(number6 * 1000 + number5 * 100 + number7 * 10 + number4)
# 1342
elif number5 > number4 > number7 > number6:
    print(number6 * 1000 + number7 * 100 + number4 * 10 + number5)
# 1234
elif number4 > number7 > number5 > number6:
    print(number6 * 1000 + number5 * 100 + number7 * 10 + number4)
# 3241
elif number6 > number5 and number4 == number7:
    print(number5 * 1000 + number4 * 100 + number4 * 10 + number6)
