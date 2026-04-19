import sys
import heapq
n,l = list(map(int,sys.stdin.readline().split()))
ways = [[] for i in range(n+l+1)]

for i in range(l):
    ways[i] = list(map(int,sys.stdin.readline().split()))[:-1]
    for j in range(len(ways[i])):
        ways[i][j]+=l
        ways[ways[i][j]].append(i)
        

st,ed = list(map(int,sys.stdin.readline().split()))
if(st==ed):
    print(0)
else:
    on=1
    bang = [1]*(n+l+1)
    q = [(0,l+st)]
    bang[q[0][1]]=0
    while q:
        qpop = heapq.heappop(q)
        if(qpop[1]==ed+l):
            print(qpop[0]-1)
            on=0
            break
        #print(qpop)
        for i in ways[qpop[1]]:
            if(bang[i]):
                bang[i]=0
                heapq.heappush(q,(qpop[0]+1*(qpop[1]<l),i))
    if(on):print(-1)