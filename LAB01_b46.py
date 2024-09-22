# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:25:09 2024

@author: Student
"""

bo_nghiem = []
for x in range (1,490):
    for y in range (1,140):
        for z in range (1,110):
            bo_nghiem = (x,y,z)
if bo_nghiem:
    print(f"{bo_nghiem}")