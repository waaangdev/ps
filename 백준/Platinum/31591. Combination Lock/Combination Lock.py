import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

n = int(sys.stdin.readline())

li = [[] for i in range(50)]
li[0] = [1]
pri = []
for i in range(2,51):
    if(li[i-1]==[]):
        pri.append(i)
        for j in range(i,51,i):
            li[j-1].append(i)
#print(li,pri)
pri = {pri[i]:i for i in range(len(pri))}
#print(pri)

li2 = []
for i in range(n):
    li2.append(list(map(int,sys.stdin.readline().split())))

dp = [[0 for i in range(2**15)] for i in range(50)]


li[0] = 0
for i in range(1,len(li)):
    li[i] = sum([2**pri[j] for j in li[i]])
#print(li,li2)

rl = []
def sol(idx,bang):
    #print(idx,bin(bang))
    if(idx == n):
        return 1
    if(dp[idx][bang]):
        return 0
    for i in range(li2[idx][0],li2[idx][1]+1):
        if(bang&li[i-1] == 0):
            if(sol(idx+1,bang+li[i-1])):
                rl.append(i)
                return 1
    dp[idx][bang] = 1
    return 0

sol(0,0)
if(rl):
    print(*rl[::-1])
else:
    print(-1)