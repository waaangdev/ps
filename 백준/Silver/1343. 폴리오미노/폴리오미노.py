import sys
from collections import deque
import math

li = sys.stdin.readline().strip()
a = 0
r = ""
for i in li:
    if(i == '.'):
        if(a == 2):
            r+="BB"
            a =0
        elif(a != 0):
            r = "-1"
            a = -1
            break
        r+="."
    if(i == 'X'):
        a+=1
        if(a == 4):
            r+="AAAA"
            a = 0
if(a == 2):
    r+="BB"
elif(a!=0):
    r="-1"
print(r)