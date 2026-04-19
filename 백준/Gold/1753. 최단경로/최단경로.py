import sys
import heapq

n,wayc = map(int,sys.stdin.readline().strip().split())
st = int(input())-1
way = [[] for i in range(n)]
for i in range(wayc):
    inp = list(map(int,sys.stdin.readline().strip().split()))
    way[inp[0]-1].append([inp[2],inp[1]-1])


q = []
heapq.heappush(q,(0,st))
dp = [200001]*n
dp[st] = 0
while(q):
    qg = list(heapq.heappop(q))
    for i in way[qg[1]]:
        if(dp[i[1]] > dp[qg[1]]+i[0]):
            dp[i[1]] = dp[qg[1]]+i[0]
            heapq.heappush(q,(dp[i[1]],i[1]))
for i in dp:
    if(i==200001): print("INF")
    else: print(i)
