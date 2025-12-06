from math import sqrt

a = float(input())
b = float(input())

s1 = (a + b) / 2  # Среднее арифметическое
s2 = sqrt(a * b)  # Среднее геометрическое
s3 = (2 * a * b) / (a + b)  # Среднее гармоническое
s4 = sqrt((a**2 + b**2) / 2)  # Среднее квадратичное

print(s1)
print(s2)
print(s3)
print(s4)