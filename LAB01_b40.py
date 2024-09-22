# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:55:41 2024

@author: Student
"""

n = int(input("Nhap N: "))
while n<=0:
    print("Nhap N: ")
s = 0
for i in range (1,n+1):
    s += 1/(2*i)
print(s)