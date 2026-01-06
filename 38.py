# объявление функции
def print_sorted_hyphen(s):
    l = sorted(s.split("-"))
    print("-".join(l))

# считываем данные
s = input()

# вызываем функцию
print_sorted_hyphen(s)