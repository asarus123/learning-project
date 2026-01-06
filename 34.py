# Делает алфавит строчных английских букв с количеством букв равным номеру буквы в алфавите.
l = []
for i in range(97, 123):
    l.append(chr(i))
for c in range(len(l)):
    l[c] = l[c] * (c+1)
print(l)