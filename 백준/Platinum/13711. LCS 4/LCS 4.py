#LCS 4
import sys
from collections import deque

n = int(input())
li = [[],[]]
li[0] = list(map(int,sys.stdin.readline().strip().split()))
li[1] = list(map(int,sys.stdin.readline().strip().split()))

li2 = [0]*n
li3 = [0]*n

for i in range(n):
    li2[li[1][i]-1] = i

for i in range(n):
    li3[i] = li2[li[0][i]-1] 

#print(li3)

dp = [0,0,0]
dp[0] = [1]*n
dp[1] = [-1]*(n+1)
dp[2] = 0

for i in range(n):
    if(dp[2] != 0):
        p1,p2 = 0,dp[2]
        while (p1+1<p2):
            dum = (p1+p2)//2
            if(li3[i] < dp[1][dum]):
                p2 = dum
            else:
                p1 = dum
        if(p1+1==p2):
            #print(p1,p2)
            dp[0][i] = p1+1
    if(dp[1][dp[0][i]] == -1):
        dp[1][dp[0][i]] = li3[i]
        dp[2] = dp[0][i]+1
    dp[1][dp[0][i]] = min(dp[1][dp[0][i]],li3[i])
#print(dp[0])
#print(dp[1])
print(max(dp[0]))