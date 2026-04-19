
import sys
from collections import deque

ang = ['N','E','S','W']

ang2 = 0

for i in range(10):
    a= int(input())
    if(a == 1):
        ang2 += 1
    elif(a == 2):
        ang2 += 2
    else:
        ang2 -=1

print(ang[ang2%4])