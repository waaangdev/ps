import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
n,m = list(map(int,sys.stdin.readline().split()))
homes = []
shops = []
for i in range(n):
    dli = list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        if(dli[j] == 1):
            homes.append([i,j])
        if(dli[j] == 2):
            shops.append([i,j])
r = 10000000000
for i in range(2**13):
    dn = bin(i)[::-1]+"000000000000000"
    if(dn.count('1')==m):
        dum = 0
        for j in homes:
            dum2 = 10000000000
            for k in range(len(shops)):
                if(dn[k]=='1'):
                    dum2 = min(dum2,abs(j[0]-shops[k][0])+abs(j[1]-shops[k][1]))
            dum+=dum2
        r = min(r,dum)
print(r)