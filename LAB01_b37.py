# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:11:15 2024

@author: Student
"""

n = int(input("Nhap N: "))
while n<=0:
    print("Nhap N: ")
s = 0
#for i in range (2,n+1,2):
for i in range (2,n+1):
    if i%2 == 0:
        s += i
print(s)