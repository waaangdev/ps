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


n,q =list(map(int,sys.stdin.readline().split()))
ways=[0]*n
def ll(a):
    if(a=='B1'):
        return 0
    if(a[0]=='B'):
        return -int(a[1:])+1
    return int(a)
def ll2(a):
    if(a==0):
        return 'B1'
    if(a<0):
        return 'B'+str(-a+1)
    return str(a)


for i in range(n-1):
    a,b = list(map(ll,sys.stdin.readline().split()))
    ways[i+1]=ways[i]+(a-b)
for i in range(q):
    a,b,c = list(map(ll,sys.stdin.readline().split()))
    print(ll2(c+(ways[a-1]-ways[b-1])))