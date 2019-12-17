import math
 
 
def f(x):
    return math.e**x + x - 3
 
 
def MPD(f, a, b, eps=1e-5):
    while abs(b - a) > eps:
        x = (a + b) / 2.0
        fx = f(x)
        fa = f(a)
        if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
            a = x
        else:
            b = x
    return x
 
 
x = MPD(f, 0, 1)
print(x)
print(f(x))
