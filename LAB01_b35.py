# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:05:51 2024

@author: Student
"""

n = int(input("Nhap N: "))
while n<=0:
    n = int(print("Nhap N: "))
s = 0
for i in range (1,n+1):
    s += i
print(s)