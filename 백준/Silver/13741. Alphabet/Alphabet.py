import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

sys.setrecursionlimit(100001)

li = sys.stdin.readline().strip()
dp = [ord(li[i])-ord('a') for i in range(len(li))]

for i in range(len(li)):
    for j in range(i):
        if(ord(li[i]) > ord(li[j])):
            dp[i] = min(dp[i],dp[j]+ord(li[i])-ord(li[j])-1)
print(min([dp[i]+ord('z')-ord(li[i]) for i in range(len(li))]))