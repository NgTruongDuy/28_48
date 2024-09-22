# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:16:22 2024

@author: Student
"""

n = int(input("Nhap N: "))
while n<=0 or n%2==0:
    print("Nhap N: ")
s = 1
for i in range (1,n+1):
    s *= i
print(s)