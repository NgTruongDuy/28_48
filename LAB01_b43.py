# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:29:29 2024

@author: Student
"""
n = int(input("Nhap N: "))
while n<=0:
    print("Nhap N: ")
s = 0
for i in range (1,n+1):
    s += i/(i+1)
print(s)