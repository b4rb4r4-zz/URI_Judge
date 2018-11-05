# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:25:29 2018

@author: bgfar
"""
h1,m1,h2,m2 = map(int, input().split())

if h1 < h2:
    horas = h2 - h1
elif h1> h2:
    horas = 24-(h1-h2)
else:
    horas = 0
    minu = m2 -m1

if m1>m2:
    minu = 60 - (m1-m2)
    if h1 < h2:
        horas = (h2- h1)-1
    elif h1> h2:
        horas = 24-(h1-h2)-1    
       
else:
    minu = m2-m1

if h1 == h2 and m1 ==m2:
    horas = 24

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas,minu))