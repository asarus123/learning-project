a = int(input())
b = a // 100
c = a % 10
d = (a % 100) // 10
m = min(b, c, d)
M = max(b, c, d)
if ((M - m) == b or (M - m) == c or (M - m) == d) and (a % 10) != 0 and b != c and c != d and b != d :
    print("Число интересное")
else :
    print("Число неинтересное")