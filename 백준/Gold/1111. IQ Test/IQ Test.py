import sys
from collections import deque

d = int(input())

li = list(map(int,input().split()))

if(d < 3):
    if(d == 2 and li[0] == li[1]):
        print(li[0])
    else:
        print("A")
else:
    if(li[1]-li[0] == 0):
        a = 0
    else:
        a = (li[2]-li[1])//(li[1]-li[0])
    b = li[1]-li[0]*a
    c = 0
    for i in range(d-1):
        if(li[i]*a+b == li[i+1]):
            pass
        else:
            c = 1   
    if(c == 0):
        print(li[d-1]*a+b)
    else:
        print("B")
        