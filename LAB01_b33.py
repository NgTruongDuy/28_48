# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:35:38 2024

@author: Student
"""

import math
n = int(input("Nhap N: "))
while n<=0:
    print("Nhap N: ")
s = int(math.sqrt(n))
if s**2 == n:
    print("So chinh phuong")
else:
    print("Khong phai so chinh phuong")
    
        
