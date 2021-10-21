import math
n = int(input())
x = float(input())
P = 0
pp = 0
while n >= 0:
    a = float(input())
    i = 0
    xn = 1
    while i < n:
        xn *= x
        i += 1
    pp = a * xn
    n -= 1
    P += pp
print(P)
