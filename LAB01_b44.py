# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:49:40 2024

@author: Student
"""

n = int(input("Nhap N: "))
while n<=0:
    print("Nhap N: ")
s = 1/2
for i in range (1,n+1):
    s += (2*i+1)/(2*i+2)
print(s)