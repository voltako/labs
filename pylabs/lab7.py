# -*- coding: utf-8 -*-
from math import *
a = str(input("Введите a: "))
x= str(input("Введите x: "))
p=str(input("Введите сколько считать:"))
h=str(input("Введите шаг:"))
shab=input("Введите шаблон: ")
listG=[]
listF=[]
listY=[]
listA=[]
listX=[]
data=[]
data1=[]
data2=[]
data3=[]
if (a != 0) or (x != 0) or ((10*a*a -51*a*x+5*x*x)!=0) :
    for i in range(int(p)):
        a = float(a)
        x = float(x)
        h = float(h)
        G = (3*(4*a*a +13*a*x+9*x*x))/(10*a*a -51*a*x+5*x*x)
        data1.append((x,a,G))
        listG.append(G)
        F = cos(6*a*a +a*x-2*x*x)
        data2.append((x,a,F))
        listF.append(F)
        if ((a == -2,5) and (x == 1)):
            Y = acos(14*a*a+37*a*x+5*x*x+1)
            data3.append((x,a,Y))
            listY.append(Y)
        a+=h
else:
    print('ERROR')
fun = input("Введите функцию которую вы хотите вывести(G,F,Y): ")
output = str(input('Как выводить? (таблица/строка): '))

if (output == 'строка'):
    if (fun == 'G'):
        print(data1)
        print('Максимальное значение: {}'.format(max(list(elem)[2] for elem in data1)))
        print('Минимальное значение: {}'.format(min(list(elem)[2] for elem in data1)))
        my_file=open('lab7.txt','w')
        my_file.write(str(data1))
        my_file.close()
        data1.clear()
        my_file=open('lab7.txt')
        my_file.read()
    if (fun == 'F'):
        print(data2)
        print('Максимальное значение: {}'.format(max(list(elem)[2] for elem in data2)))
        print('Минимальное значение: {}'.format(min(list(elem)[2] for elem in data2)))
        my_file=open('lab7.txt','w')
        my_file.write(str(data2))
        my_file.close()
        data.clear()
        my_file=open('lab7.txt')
        my_file.read()
    if (fun == 'Y'):
        print(data3)
        print('Максимальное значение: {}'.format(max(list(elem)[2] for elem in data3)))
        print('Минимальное значение: {}'.format(min(list(elem)[2] for elem in data3)))
        my_file=open('lab7.txt','w')
        my_file.write(str(data2))
        my_file.close()
        data3.clear()
        my_file=open('lab7.txt')
        my_file.read()
elif (output == 'таблица'):
    q = 0
    if (fun == 'G'):
        for i in listG:
            print('a = {} x = {} g = {}'.format(str(list(elem)[0] for elem in data1),str(list(elem)[1] for elem in data1),str(list(elem)[2] for elem in data1)))
            i += 1
            q += 1
    if (fun == 'F'):
        for i in listF:
            print('a = {} x = {} g = {}'.format(str(list(elem)[0] for elem in data2),str(list(elem)[1] for elem in data2),str(list(elem)[2] for elem in data2)))
            i += 1
            q += 1
    if (fun == 'Y'):
        for i in listY:
            print('a = {} x = {} g = {}'.format(str(list(elem)[0] for elem in data3),str(list(elem)[1] for elem in data3),str(list(elem)[2] for elem in data3)))
            i += 1
            q += 1
else:
    print('ERROR')
shab=float(shab)
if (fun == 'G'):
    print('Кол-во совпадений: {}'.format(listG.count(shab)))
elif (fun == 'F'):
    print('Кол-во совпадений: {}'.format(listF.count(shab)))
elif (fun == 'Y'):
    print('Кол-во совпалений: {}'.format(listY.count(shab)))
else:
    print('ERORR')

