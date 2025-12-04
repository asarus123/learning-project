a = int(input())
c = int(input())
b = input()

if b == "+" :
    d = a + c
    print(d)
elif b == "-" :
    d = a - c
    print(d)
elif b == "*" :
    d = a * c
    print(d)
elif b == "/" :
    if c == 0 :
        print("На ноль делить нельзя!")
    else :
        d = (a / c)
        print(d)
else :
    print("Неверная операция")
