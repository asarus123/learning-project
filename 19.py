n = int(input())
counter = 0
while n >= 25:
    counter += 1
    n -= 25
while 25 > n >= 10:
    counter += 1
    n -= 10
while 10 > n >= 5:
    counter += 1
    n -= 5
while 5 > n >= 1:
    counter += 1
    n -= 1
print(counter)