# Даётся никнейм. Проверяется, начинается ли он с @, имеет ли от 5 до 15 символов включительно, состоит ли только из строчных букв и цифр.
s = input()
s1 = s.lower()
s2 = s[1:]
if s.startswith("@") and 5 <= len(s) <= 15 and s == s1 and s2.isalnum():
    print("Correct")
else:
    print("Incorrect")