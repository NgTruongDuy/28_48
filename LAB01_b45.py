# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:52:53 2024

@author: Student
"""

x = float(input("Nhap X: "))
n = int(input("Nhap N: "))
while n<=0:
    print("Nhap N: ")

ts = 0
ms = 0    
s = 0
for i in range (1,n+1):
    ts = x**i
    ms = ms + i
    s += ts/ms
print(s)