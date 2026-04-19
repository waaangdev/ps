import sys
from collections import deque
sys.setrecursionlimit(200001)

n,m = map(int,sys.stdin.readline().strip().split())
ways = [[] for i in range(n)]
for i in range(m):
    inp=list(map(int,sys.stdin.readline().strip().split()))

    ways[inp[0]-1].append(inp[1]-1)
    ways[inp[1]-1].append(inp[0]-1)

dp = [-1 for i in range(n)]

q = deque([0])
dp[0] = 1
while q:
    lenq = len(q)
    for _ in range(lenq):
        qpop = q.popleft()
        for i in range(len(ways[qpop])):
            if(dp[ways[qpop][i]] == -1):
                dp[ways[qpop][i]]  = dp[qpop]+1 
                q.append(ways[qpop][i])

#print(dp)
bang2 = [0 for i in range(n)]
q = deque([n-1])
bang2[n-1] = 1
rl = []
while q:
    lenq = len(q)
    #print(q)
    if(lenq==1):
        dum = q.pop()
        rl.append(dum)
        q.append(dum)
    for _ in range(lenq):
        qpop = q.popleft()
        for i in range(len(ways[qpop])):
            if(dp[ways[qpop][i]] == dp[qpop]-1):
                if(bang2[ways[qpop][i]] == 0):
                    bang2[ways[qpop][i]] = 1
                    q.append(ways[qpop][i])
# print(rl)
if(len(rl)!=2):
    for i in rl:
        if(i!= 0 and i!= n-1):
            print(i+1)
            break
else:
    print(1)