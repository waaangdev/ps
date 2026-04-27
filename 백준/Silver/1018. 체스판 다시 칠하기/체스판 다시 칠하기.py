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

n,m1 = list(map(int,sys.stdin.readline().split()))
m = []
for i in range(n):
    m.append(sys.stdin.readline().strip())

r = 64
for i in range(n-8+1):
    ok,no = 0,0
    for j in range(8):
        for k in range(8):
            if("BW"[(i+j+k)%2] == m[i+j][k]):
                ok+=1
            else:
                no+=1
    r=min([r,ok,no])
    for j in range(m1-8):
        for k in range(8):
            if("BW"[(i+j+k)%2] == m[i+k][j]):
                ok-=1
            else:
                no-=1
        for k in range(8):
            if("BW"[(i+j+k)%2] == m[i+k][j+8]):
                ok+=1
            else:
                no+=1
        r=min([r,ok,no])
print(r)