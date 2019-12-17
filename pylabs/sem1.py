import math
a = float(input('Введите число: '))
def func (a):
    x = 3
    b = 0
    if (a<0):
        raise ValueError('введите норм число')
    while b != (a**0.5):
        b = 0.5 * (x + a/x)
        x = b
        print(b,x)
    return(b)
print('мой ответ: ',func(a))
print('ответ встроенной ф-ии: ',math.sqrt(a))
print('Точность равна: ',(math.sqrt(a)-func(a)))
