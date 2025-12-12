# Проверяет наличие в числе четных цифр и выводит их
num = int(input())
n = len(str(num))
counter = 0
co2 = 0
for i in range(1, n+1):                         
    digit = num // 10 ** (n - i) % 10
    if digit % 2 == 0:
        co2 += 1
        print(co2, "-я четная цифра равна ", digit, sep="")
    else:
        counter+= 1
if counter == n:
    print("Четных цифр в числе нет")