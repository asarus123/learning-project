# Вводится число строк, затем сами строки, затем строка поискового запроса. Вывлодятся все строки, в которых содержится строка поискового запроса.
n = int(input())
l = []
for i in range(n):
    l.append(input())
s = input()
for c in range(len(l)):
    if s.lower() in l[c].lower():
        print(l[c], end="\n")