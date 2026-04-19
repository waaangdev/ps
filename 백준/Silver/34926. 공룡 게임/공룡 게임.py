import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n,k = list(map(int,sys.stdin.readline().split()))
li = sys.stdin.readline().strip()
dp = [0 for i in range(n)]
dp[0] = 1
for i in range(1,n):
    if(li[i] == '_'):
        dp[i] = max(dp[i-1],dp[i-k])
print(["NO","YES"][dp[n-1]])