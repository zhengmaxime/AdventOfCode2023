from math import sqrt

l = open('f').readlines()
t = ''.join(l[0].split(':')[1].split())
d = ''.join(l[1].split(':')[1].split())

a = -1
b = int(t)
c = -int(d)
delta = b*b - 4*a*c
x1 = (-b-sqrt(delta)) / 2*a
x2 = (-b+sqrt(delta)) / 2*a
print(int(x1-x2))


"""
x(71530 - x) > 940200
71530x - x*x > 940200
-x*x + 71530x - 940200 > 0

a = -1
b = +71530
c = -940200
"""
