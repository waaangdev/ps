import sys
import heapq

n,wayc = map(int,sys.stdin.readline().strip().split())
way = [[] for i in range(n)]
for i in range(wayc):
    inp = list(map(int,sys.stdin.readline().strip().split()))
    way[inp[0]-1].append([inp[2],inp[1]-1])
    way[inp[1]-1].append([inp[2],inp[0]-1])

input()
homes=list(map(int,sys.stdin.readline().strip().split()))
shops=list(map(int,sys.stdin.readline().strip().split()))
homes.sort()

q = []
dp = [10000*1000000]*n
for i in shops:
    heapq.heappush(q,(0,i-1))
    dp[i-1] = 0

while(q):
    #print(q)
    qg = list(heapq.heappop(q))
    for i in way[qg[1]]:
        if(dp[i[1]] > dp[qg[1]]+i[0]):
            dp[i[1]] = dp[qg[1]]+i[0]
            heapq.heappush(q,(dp[i[1]],i[1]))

mins = 10000*1000000
mini = -1
for i in homes:
    if(mins > dp[i-1]):
        #print(mins,i)
        mins=dp[i-1]
        mini = i
print(mini)
