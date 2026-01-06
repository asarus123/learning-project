l = input().split("-")
if l[0] == "7":
    del l[0]
    if len(l[0]) == 3 and len(l[1]) == 3 and len(l[2]) == 4 and "".join(l).isdigit() == True:
        print("YES")
    else:
        print("NO")
elif len(l[0]) == 3 and len(l[1]) == 3 and len(l[2]) == 4 and "".join(l).isdigit() == True:
    print("YES")
else:
    print("NO")