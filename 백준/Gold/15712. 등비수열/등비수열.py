import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

a,r,n,mod=list(map(int,sys.stdin.readline().split()))
if(r==1):
    print(a*n%mod)
else:
    #a(r^n-1)//(r-1)


    #r*(1/r) = 1


    def rn(r,n,mod):
        if(n == 0):return 1
        if(n ==1):return r
        if(n%2==0):
            return (rn(r,n//2,mod)**2)%mod
        else:
            return (rn(r,n//2,mod)**2*r)%mod

    rs = 0
    cho = a
    r100 = rn(r,100,mod)
    for i in range(100):
        rs+=cho
        rs%=mod
        cho*=r
        cho%=mod
    
    rr = 0
    for i in range(n//100):
        rr+=rs
        rr%=mod
        rs*=r100
        rs%=mod

    cho = a*rn(r,n-n%100,mod)%mod
    for i in range(n%100):
        rr+=cho
        rr%=mod
        cho*=r
        cho%=mod

    print(rr)