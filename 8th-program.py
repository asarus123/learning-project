a = int(input())
b = int(input())
c = int(input())
if a == b == c :
    print("Равносторонний")
elif (a == b != c) or (a == c != b) or (b == c != a) :
    print("Равнобедренный")
elif a != b and b != c and a != c :
    print("Разносторонний")