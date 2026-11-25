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

n,m = list(map(int,input().split()))
maps = []
for i in range(n):
    maps.append(list(map(int,input().split())))
#maps=list(reversed(maps))
dps = [[[-1000000000000 for i in range(m)] for i in range(n)] for i in range(2)]

for i in range(2):
    dps[i][n-1][0] = maps[n-1][0]
    for j in range(n-1,-1,-1):
        for k in range(m):

            if(j<n-1):dps[i][j][k] = max(dps[i][j][k],maps[j][k]+dps[i][j+1][k])
            if(k>0):dps[i][j][k] = max(dps[i][j][k],maps[j][k]+dps[i][j][k-1])
    for j in range(n-1,-1,-1):
        maps[j]=list(reversed(maps[j]))

rr = dps[0][0][0]+dps[1][0][m-1]
for i in range(n):
    for j in range(m):
        rr= max(rr,dps[0][i][j]+dps[1][i][m-j-1])
# for i in dps[0]:
#     print(i)
# print()
# for i in dps[1]:
#     print(list(reversed(i)))
print(rr)