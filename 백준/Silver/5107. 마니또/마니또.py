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

idx=0
while 1:
    idx+=1
    n = int(sys.stdin.readline())
    if(not n):break
    ways = {}
    dp = {}
    r=0
    for i in range(n):
        inp = sys.stdin.readline().strip().split()
        ways[inp[0]]=inp[1]
        dp[inp[0]]="-1"
    for i in ways.keys():
        st = i
        while 1:
            if (dp[st]=="-1"):
                dp[st]=i
            elif(dp[st]==i):
                r+=1
                break
            else:
                break
            st = ways[st]
    print(idx,r)