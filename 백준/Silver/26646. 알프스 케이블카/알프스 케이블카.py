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

#강현준이정해스포함;;


n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

dp = [[-1,-1] for i in range(101)]
dp[li[0]]=[0,li[0]]
x = li[0]*2
mins =0
for i in range(1,n):
    x+=li[i]
    mins = -1
    for j in range(101):
        if(dp[j][0]!=-1):
            if(mins==-1):
                mins = dp[j][0]+(j-li[i])**2+(dp[j][1]-x)**2
            else:
                mins=min(mins,dp[j][0]+(j-li[i])**2+(dp[j][1]-x)**2)
    dp[li[i]]=[mins,x]
    x+=li[i]
print(mins)
