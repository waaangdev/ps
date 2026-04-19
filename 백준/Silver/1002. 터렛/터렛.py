
import sys
from collections import deque
import math

a = int(sys.stdin.readline())

for i in range(a):
    b,c,d,e,f,g = map(int,sys.stdin.readline().split())
    h = math.sqrt((b-e)**2+(c-f)**2)
    if(h > d+g):
        print(0)
    elif(h == d+g):
        print(1)
    else:
        if([b,c] == [e,f]):
            if(d == g):
                print(-1)
            else:
                print(0)
        else:
            if(d>h+g):
                print(0)
            elif(d==h+g):
                print(1)
            elif(g>h+d):
                print(0)
            elif(g==h+d):
                print(1)
            else:
                print(2)