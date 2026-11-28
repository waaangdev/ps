import sys
from collections import deque
import random
import math
import heapq #minheap

input = lambda: sys.stdin.readline().rstrip()
print = lambda *a,end='\n': sys.stdout.write(' '.join(map(str,a))+end)

#n = int(input())
#li = list(map(int,input().split()))

sys.setrecursionlimit(100010)
sys.set_int_max_str_digits(101000)

n,m = list(map(int,input().split()))
s,e = list(map(int,input().split()))
li = [0 for i in range(n)]
li[s-1]=1

if(n==2):
    print((s==e)^(m%2))
else:
    for i in range(m):
        lihis = li[:]
        d = (1/(n-1))
        for j in range(n):
            if(j==0):
                li[j] = lihis[j+1]*d+ lihis[j]*(1-d)
            elif(j==n-1):
                li[j] = lihis[j-1]*d+ lihis[j]*(1-d)
            else:
                li[j] = lihis[j-1]*d+lihis[j+1]*d+ lihis[j]*(1-2*d)
    print(li[e-1])