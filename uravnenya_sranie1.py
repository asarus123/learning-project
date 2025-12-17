# 28n+30k+31m=365
for n in range(1, 14):
    for k in range(1, 13):
        for m in range(1, 12):
            if 28*n + 30*k + 31*m ==365:
                print("n =", n, "k =", k, "m =", m)

