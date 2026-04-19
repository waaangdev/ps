import sys
from collections import deque

# dp = [-1 for i in range(1000)]
# def sol(n):#이기는가
#     if(dp[n] !=-1): return dp[n]
#     for i in range(1,n+1):
#         if(str(i) == str(i)[::-1]):
#             if(sol(n-i) == False):
#                 dp[n] = 1
#                 return True
#     dp[n] = 0
#     return False

# for i in range(1,100):
#     print(i,sol(i))

for _ in range(int(input())):
    print(0+1*(int(input())%10==0))