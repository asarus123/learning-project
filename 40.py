# объявление функции
def math_round_to_int(num):
    return int(num + 0.5)

# считываем данные
num = float(input())

# вызываем функцию
print(math_round_to_int(num))