a = input()
b = input()

if a == b == "красный" :
    print("красный")
elif a == b == "синий" :
    print("синий")
elif a == b == "желтый" :
    print("желтый")
elif (a == "красный" and b == "синий") or (b == "красный" and a == "синий") :
    print("фиолетовый")
elif (a == "красный" and b == "желтый") or (b == "красный" and a == "желтый") :
    print("оранжевый")
elif (a == "желтый" and b == "синий") or (b == "желтый" and a == "синий") :
    print("зеленый")
else :
    print("ошибка цвета")