# объявление функции
def get_unique(numbers):
    l = []
    for i in range(len(numbers)):
        if numbers[i] not in l:
            l.append(numbers[i])
    return l

# считываем данные
numbers = eval(input())

# вызываем функцию
print(get_unique(numbers))