import math
x = float(input('введите значение x '))
y = float(input("введите значение y "))
zz = (((math.sqrt(abs(x)))+5*y)/math.pi+(0.55**3)*math.cos(x))**3
print(zz)