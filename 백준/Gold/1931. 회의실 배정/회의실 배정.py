import sys
from collections import deque
import math

a = int(sys.stdin.readline())
li =[]

for i in range(a):
    b,c = map(int,sys.stdin.readline().split())
    li.append([b,c])

li.sort(key = lambda x: (x[1],x[0]))


r = 0
t= 0 
while li:
    if(li[0][0] >= t):
        r+= 1
        t = li[0][1]
    del li[0]
print(r)