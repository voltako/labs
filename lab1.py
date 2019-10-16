# -*- coding: utf-8 -*-

from math import *
a = float(input("Введите a: "))
x= float(input("Введите x: "))
fun = input("Введите функцию которую вы хотите вычислить(G,F,Y): ")
if (fun == 'G'):
    G = (3*(4*a*a +13*a*x+9*x*x))/(10*a*a -51*a*x+5*x*x)
    print(G)
elif (fun == 'F'):
    F=cos(6*a*a +a*x-2*x*x)
    print(F)
elif (fun == 'Y'):
    Y=acos(14*a*a+37*a*x+5*x*x+1)
    print(Y)


