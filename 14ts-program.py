a = input()
b = input()
c = input()
la = len(a)
lb = len(b)
lc = len(c)
m = min(la, lb, lc)
M = max(la, lb, lc)
s = (la + lb + lc) - (M + m)
if (M - s) == (s - m) :
    print("YES")
else :
    print("NO")