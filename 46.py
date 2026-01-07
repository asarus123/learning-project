# объявление функции
def is_magic(date):
    dl = date.split(".")
    if int(dl[0]) * int(dl[1]) == int(dl[2]) % 100:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))