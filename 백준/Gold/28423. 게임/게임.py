import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
sys.setrecursionlimit(100021)

l,r = list(map(int,sys.stdin.readline().split()))

fdp = [-2 for i in range(100001)]

def f(n):
    if(fdp[n] == -3):
        fdp[n] = 0
        return 0
    elif(fdp[n] != -2):
        return fdp[n] 

    dum = str(sum(map(int,list(str(n)))))
    dum2 = 1
    for i in str(n):
        dum2*=int(i)
    dum+=str(dum2)

    dum = int(dum)
    if (dum > 100000):
        fdp[n] = -1
        return -1
    if(dum == n):
        fdp[n] = 1
        return 1
    fdp[n] = -3 
    fdp[n] = f(dum)
    return fdp[n]

rr = 0
for i in range(l,r+1):
    rr+=f(i)
print(rr)
    
