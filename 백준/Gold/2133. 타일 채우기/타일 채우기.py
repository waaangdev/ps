from collections import deque
import sys


sys.setrecursionlimit(101)


dp = [-1]*31

def sol(a):
    if(a == 0): return 1
    if(a < 0): return 0
    if(dp[a]!=-1):return dp[a]
    r = sol(a-2)*3
    for i in range(100):
        r+= sol(a-4-2*i)*2
    dp[a] = r
    return r


print(sol(int(input())))