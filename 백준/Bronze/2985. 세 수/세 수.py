
import sys
from collections import deque

def d(d,e,f):
    li = [d+e,d-e,d*e,d//e]
    return li[f]

a,b,c = map(int,sys.stdin.readline().split())
li2 = "+-*/"

for i in range(2):
    
    for j in range(4):
        if(i == 0):
            if(d(a,b,j) == c):
                print(str(a)+li2[j]+str(b)+"="+str(c))
        if(i == 1):
            if(d(b,c,j) == a):
                print(str(a)+"="+str(b)+li2[j]+str(c))