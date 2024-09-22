# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:55:49 2024

@author: Student
"""

n = int(input("Nhap N nguyen duong: "))
while n<=0:
    print("Nhap lai N: ")
for i in range (1,n+1):
    if n%i == 0:
        print(i,end=" ")