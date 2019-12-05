# -*- coding: utf-8 -*-

from math import *
a = float(input("Введите a: "))
x= float(input("Введите x: "))
fun = input("Введите функцию которую вы хотите вычислить(G,F,Y): ")
p=int(input("Введите сколько считать:"))
h=float(input("Введите шаг:"))
listG=[]
listF=[]
listY=[]
listA=[]
listX=[]
if (fun == 'G'):
    for i in range(p):
        G = (3*(4*a*a +13*a*x+9*x*x))/(10*a*a -51*a*x+5*x*x)
        if (10*a*a-51*a*x+5*x*x) ==0:
            print('ERROR')
        else:
            print(G)
            print()
            listG.append(G)
            listA.append(a)
            listX.append(x)
            a+=h
elif (fun == 'F'):
    for i in range(p):
        F=cos(6*a*a +a*x-2*x*x)
        if (a==0):
            print("ERROR")
        else:
            print(F)
            print()
            listF.append(F)
            listA.append(a)
            listX.append(x)
            a+=h
elif (fun == 'Y'):
    for i in range(p):
        Y=acos(14*a*a+37*a*x+5*x*x+1)
        print(Y)
        print()
        listY.append(Y)
        listA.append(a)
        listX.append(x)
        a+=h
else:
    print('ERROR')

output = str(input('Как выводить? (таблица/строка): '))

if (output == 'строка'):
    if (fun == 'G'):
        print(listG)
        print(max(listG))
        print(min(listG))
    if (fun == 'F'):
        print(listF)
        print(max(listF))
        print(min(listF))
    if (fun == 'Y'):
        print(listY)
        print(max(listY))
        print(min(listY))
elif (output == 'таблица'):
    q = 0
    if (fun == 'G'):
        for i in listG:
            print('a = {} x = {} g = {}'.format(str(listA[q]),str(listX[q]),str(listG[q])))
            i += 1
            q += 1
    if (fun == 'F'):
        for i in listF:
            print('a = {} x = {} f = {}'.format(str(listA[q]),str(listX[q]),str(listF[q])))
            i += 1
            q += 1
    if (fun == 'Y'):
        for i in listY:
            print('a = {} x = {} y = {}'.format(str(listA[q]),str(listX[q]),str(listY[q])))

            i += 1
            q += 1
else:
    print('ERROR')
