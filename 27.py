# Нахождение того, какого символа в строке больше всего.
s = input()
s1 = 0
s2 = 0
for i in range(len(s)):
    if s.count(s[i]) >= s1:
        s1 = s.count(s[i])
        s2 = s[i]
print(s2)