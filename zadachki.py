s1 = input()
s2 = ""
s = ""
while True:
    sZ = s
    s = input()
    if s == "КОНЕЦ":
        break
    if s < s1:
        s1 = s
    if s > sZ and s > s2:
        s2 = s
print(f"Минимальная строка ⬇️: {s1}")
print(f"Максимальная строка ⬆️: {s2}")