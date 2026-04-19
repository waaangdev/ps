import sys
import math
from collections import deque

dp =[[0 for i in range(301)] for i in range(301)]
n,m = map(int,input().split())

for i in range(1,301):
    for j in range(1,301):
        if(i==j and i==1): 
            dp[i][j] =0
        else:
            if(i < j):
                dp[i][j] = dp[i][j//2]+dp[i][j-j//2]+1
            else:
                dp[i][j] = dp[i//2][j]+dp[i-i//2][j]+1
print(dp[n][m])