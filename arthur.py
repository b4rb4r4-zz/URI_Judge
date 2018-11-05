# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 09:43:40e 2018

@author: bgfar
"""

'''
import math

def ulululu(a,b,c):
    delta=(b**2)-4*a*c
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    return x1,x2

for i in range(1,5):
    a=float(input())
    b=float(input())
    c=float(input())
    x1,x2 = ulululu(a,b,c)
    print('X1 =', x1)
    print('X2 =', x2)
    
'''

import numpy as np

teste = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(teste)