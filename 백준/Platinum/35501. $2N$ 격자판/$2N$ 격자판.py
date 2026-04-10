import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

sys.setrecursionlimit(100001)

n= int(sys.stdin.readline())

maps2 = [list(sys.stdin.readline().strip()),list(sys.stdin.readline().strip())]
dp =[[[-1]*n for i in range(2)] for i in range(2)]

def sol(x,y,d):
    if(dp[d][x][y]==-1):
        dp[d][x][y] = 500000
        r = 0
        for i in range(y,n):
            for j in range(2):
                if(maps[j][i]=='X'):
                    if(i!=y or not d):
                        if([i,j] != [y,x]):
                            dp[d][x][y] = min(dp[d][x][y],sol(j,i,i==y)+max(0,abs(x-j)+abs(i-y))-1)
                            r=1
            if(r):break
        if(r==0):
            dp[d][x][y]=0
    return dp[d][x][y]

rr = 4000000000
for maps in [maps2,[maps2[0][::-1],maps2[1][::-1]]]:
    if('S' in maps[1]):
        maps = maps[::-1]
    sidx = maps[0].index('S')
    
    dr = 0
    sidy = 0
    if('X' in maps[0]):
        xidx = maps[0].index('X')
        if(xidx < sidx):

            while sidx!=xidx:
                sidx-=1
                if(maps[0][sidx]=='O'):
                    dr += 1
                else:
                    maps[0][sidx]='O'
    r =0
    dr2 = 400000000000000000
    for i in range(n):
        for j in range(2):
            if(maps[j][i]=='X'):
                dp =[[[-1]*n for i in range(2)] for i in range(2)]
                dr2=min(dr2,max(0,abs(sidx-i)+abs(sidy-j)-1)+sol(j,i,0))
                r=1

        if(r):break
    dr+=dr2
    rr = min(rr,dr)
print(rr)