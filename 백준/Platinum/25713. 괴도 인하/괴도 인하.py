import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li1 = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

#sys.setrecursionlimit(100001)

n,m= list(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline())

maps = [[[0,0,0,0] for i in range(m+1)] for i in range(n+1)]

for _ in range(k):
    y1,x1,y2,x2 = list(map(int,sys.stdin.readline().split()))
    #1:옆,2위,3엽-,4위-
    for i in range(y1-1,y2):
        maps[i][x1-1][0] += 1

    for i in range(x1-1,x2):
        maps[y1-1][i][1] += 1


dp =  [[-1 for i in range(m)] for i in range(n)]
dp[0][0]=min(maps[0][0][0],maps[0][0][1])
for i in range(n):
    for j in range(m):
        if(dp[i][j]==-1):
            mins = 1000000
            if(j!=0): mins=min(mins,dp[i][j-1]+maps[i][j][0])
            if(i!=0): mins=min(mins,dp[i-1][j]+maps[i][j][1])
            dp[i][j]=mins
    #print(dp[i])
print(dp[n-1][m-1])