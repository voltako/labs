# -*- coding: utf-8 -*-
from collections import namedtuple
from math import *
a = str(input("Введите a: "))
x= str(input("Введите x: "))
p=str(input("Введите сколько считать:"))
h=str(input("Введите шаг:"))
shab=float(input("Введите шаблон: "))
listG=[]
listF=[]
listY=[]
listA=[]
listX=[]
data=[]
data1=[]
data2=[]
data3=[]
if (a != 0) or (x != 0):
    for i in range(int(p)):
        a = float(a)
        x = float(x)
        h = float(h)
        G = (3*(4*a*a +13*a*x+9*x*x))/(10*a*a -51*a*x+5*x*x)
        data1.append(G(G),a(a),x(x))
        F = cos(6*a*a +a*x-2*x*x)
        data2.append((x,a,F))
        #if ((14*a*a+37*a*x+5*x*x+1) <= pi/2):
         #   data3.append((x,a))
        #else:
         #   Y = acos(14*a*a+37*a*x+5*x*x+1)
          #  data3.append((x,a,Y))
        a+=h
else:
    print('ERROR')
fun = input("Введите функцию которую вы хотите вывести(G,F,Y): ")
output = str(input('Как выводить? (таблица/строка): '))

if (output == 'строка'):
    if (fun == 'G'):
        data=(data1[G]) 
        print(data1)
        print('Максимальное значение: {}'.format(max(data)))
        print('Минимальное значение: {}'.format(min(data)))
    if (fun == 'F'):
        print(data2)
        #print('Максимальное значение: {}'.format(max(listF)))
        #print('Минимальное значение: {}'.format(min(listF)))
    if (fun == 'Y'):
        print(data3)
        #print('Максимальное значение: {}'.format(max(listY)))
        #print('Минимальное значение: {}'.format(min(listY)))
#elif (output == 'таблица'):
#    q = 0
#    if (fun == 'G'):
#        for i in listG:
#            print('a = {} x = {} g = {}'.format(str(listA[q]),str(listX[q]),str(listG[q])))
#            i += 1
#            q += 1
#    if (fun == 'F'):
#        for i in listF:
 #           print('a = {} x = {} f = {}'.format(str(listA[q]),str(listX[q]),str(listF[q])))
  #          i += 1
   #         q += 1
    #if (fun == 'Y'):
     #   for i in listY:
      #      print('a = {} x = {} y = {}'.format(str(listA[q]),str(listX[q]),str(listY[q])))
#
 #           i += 1
  #          q += 1
#else:
 #   print('ERROR')
#if (fun == 'G'):
 #   print('Кол-во совпадений: {}'.format(listG.count(shab)))
#elif (fun == 'F'):
 #   print('Кол-во совпадений: {}'.format(listF.count(shab)))
#elif (fun == 'Y'):
 #   print('Кол-во совпалений: {}'.format(listY.count(shab)))
#else:
 #   print('ERORR')

