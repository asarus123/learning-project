a = int(input())
if a == 0 :
    print("зеленый")
elif a == 1 or a == 3  or a == 5  or a == 7  or a == 9  or a == 12  or a == 14  or a ==16  or a == 18  or a == 19  or a == 21  or a == 23  or a == 25  or a == 27  or a == 30  or a == 32  or a == 34  or a == 36 :
    print("красный")
elif 0 < a < 37 :
    print("черный")
else :
    print("ошибка ввода")