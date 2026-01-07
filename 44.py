# объявление функции
def convert_to_python_case(text):
    s = ""
    for i in range(len(text)):
        if i == 0:
            s += text[i].lower()
            continue
        if text[i].isupper() == True and i != 0:
            s+="_"
            s+=text[i].lower()
        else:
            s+=text[i]
    return s

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))