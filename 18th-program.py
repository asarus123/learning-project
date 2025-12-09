# Величайший код в истории нахуй
n = int(input())
flag1 = 1
flag2 = 1
if n == 1 :
    print("1")
elif n == 2 :
    print("1 1")
elif n == 3 :
    print("1 1 2")
if n > 3 :
    print("1 1 2 ", end="")
if n > 3 :
    for i in range(4, n+1):
        flag1 = flag1 + flag2
        flag2 = flag1 - flag2
        a = flag1 + flag2
        print(a, end=" ")