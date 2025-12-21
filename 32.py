# Расшифровка шифра Цезаря
n = int(input())
s = input()
for i in range(len(s)):
    d = ord(s[i])
    if d-n < 97:
        d += 26
        print(chr(d-n), end="")
    else:
        print(chr(d-n), end="")