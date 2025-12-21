# Подсчет строчных букв в строке.
s = input()
sl = s.lower()
counter = 0
for i in range(len(s)):
    if s[i] == sl[i] and s[i] not in "1234567890":
        counter+= 1
print(counter)