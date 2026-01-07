# объявление функции
def is_palindrome(text):
    t1 = text.lower()
    tl = []
    for i in range(len(t1)):
           if t1[i].isalpha():
                   tl.append(t1[i])
    if tl[:] == tl[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))