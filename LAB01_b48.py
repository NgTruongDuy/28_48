# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

min = 979
bo_nghiem = []
for x in range (1,490):
    for y in range (1,140):
        for z in range (1,110):
            if 2*x + 7*y +9*z == 979:
                tong = x+y+z
                if tong < min:
                    min = tong
                bo_nghiem = (x,y,z)
if bo_nghiem:
    print(f"{bo_nghiem} voi {x+y+z} = {min}")