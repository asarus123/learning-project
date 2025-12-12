# Проверка того, все ли цифры в числе одинаковые
n = int(input())
num = n % 10
ln = len(str(n))
counter = 0
while n > 0:
    ld = n % 10
    if ld == num :
        counter += 1
    n //= 10
if counter == ln:
    print("YES")
else:
    print("NO")