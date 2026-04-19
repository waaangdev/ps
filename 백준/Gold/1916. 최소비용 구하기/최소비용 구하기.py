import sys
import heapq
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())
ways = [[] for i in range(n+1)]
dp = [1000000000000 for i in range(n+1)]
for i in range(m):
    inp =list(map(int,sys.stdin.readline().split()))
    ways[inp[0]]+=[[inp[1],inp[2]]]
a,b =list(map(int,sys.stdin.readline().split()))
q = [(0,a)]
while q:
    #print(q)
    qpop = heapq.heappop(q)
    if(qpop[0] <= dp[qpop[1]]):
        dp[qpop[1]]=qpop[0]
    else:
        continue
    for i in ways[qpop[1]]:
        if(qpop[0]+i[1] < dp[i[0]]):
            dp[i[0]]=qpop[0]+i[1]
            heapq.heappush(q,(qpop[0]+i[1],i[0]))
print(dp[b])