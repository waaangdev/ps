import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

#sys.setrecursionlimit(100001)

n = int(sys.stdin.readline())

nli = [-1]*n
nli2 = [[]]
li = ["" for i in range(n)]

st = sys.stdin.readline().strip()
idx = 0
for i in range(n):
    for j in range(n-i):
        li[i]+=st[idx]
        idx+=1
        
def sol2(n):
    if(n<0):return '-'
    if(n>0):return '+'
    return '0'

def sol(i,j):
    global nli
    #print(i,j)
    if(i==n):return 1
    if(j == 0):
        if(li[i][0]=='0'):
            nli[i]=0
            if(sol(i,1)):return 1
            return 0
        ra = range(1,11)
        if(li[i][0]=='-'):ra=range(-1,-11,-1)

        for k in ra:
            nli[i]=k
            if(sol(i,1)):return 1
        return 0
    else:
        sums=nli[i]
        for k in range(i-1,-1,-1):
            sums+=nli[k]
            if(li[k][(i)-k] != sol2(sums)):
                return 0
        if(sol(i+1,0)):return 1
        return 0
if(sol(0,0)==0):
    print(0/0)
print(*nli)