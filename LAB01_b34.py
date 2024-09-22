# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:29:41 2024

@author: Student
"""

n = int(input("Nhap N: "))
while n<=0:
    print("Nhap N: ")
if n<2:
    print("Khong phai so nguyen to")
for i in range (2,n):
    if n%i == 0:
        print("Khong phai so nguyen to")
        break
    else:
        print("So nguyen to")
        break
        