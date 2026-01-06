# объявление функции
def print_case_counts(s):
    up = 0
    low = 0
    for i in range(len(s)):
        if s[i].isupper() == True:
            up += 1
        if s[i].islower() == True:
            low += 1
    print("Букв в верхнем регистре:", up)
    print("Букв в нижнем регистре:", low)

# считываем данные
s = input()

# вызываем функцию
print_case_counts(s)