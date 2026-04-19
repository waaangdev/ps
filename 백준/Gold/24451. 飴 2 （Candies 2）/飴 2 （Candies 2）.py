import sys
import heapq
sys.setrecursionlimit(10000)
n,k = list(map(int,sys.stdin.readline().split()))
li = list(map(int,sys.stdin.readline().split()))
dp = [[-1]*k for i in range(n)]

def sol(idx,his):
    if(idx>=n):
        return 0

    if(his ==k):
        his = 0
    if(dp[idx][his]!=-1): return dp[idx][his]
    
    dp[idx][his] = sol(idx+1,his+(1)*(his!=0))
    if(his == 0):
        dp[idx][his] = max(dp[idx][his],sol(idx+1,1)+li[idx])
    else:
        dp[idx][his] = max(dp[idx][his],sol(idx-his+k,(idx-his+k)-idx)+li[idx])
    return dp[idx][his]
print(sol(0,0))