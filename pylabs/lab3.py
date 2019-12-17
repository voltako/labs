# -*- coding: utf-8 -*-

from math import *
a = float(input("Введите a: "))
x= float(input("Введите x: "))
fun = input("Введите функцию которую вы хотите вычислить(G,F,Y): ")
p=int(input("Введите сколько считать:"))
h=float(input("Введите шаг:"))
if (fun == 'G'):
    for i in range(p):
        if (10*a*a-51*a*x+5*x*x) ==0:
            print('ERROR')
        else:
            G = (3*(4*a*a +13*a*x+9*x*x))/(10*a*a -51*a*x+5*x*x)
            print(G)
            print()
            a+=h
elif (fun == 'F'):
    for i in range(p):
        F=cos(6*a*a +a*x-2*x*x)
        if (a==0):
            print("ERROR")
        else:
            print(F)
            a+=h
elif (fun == 'Y'):
    for i in range(p):
        Y=acos(14*a*a+37*a*x+5*x*x+1) 
        print(Y)
        a+=h
else:
    print('ERROR')
