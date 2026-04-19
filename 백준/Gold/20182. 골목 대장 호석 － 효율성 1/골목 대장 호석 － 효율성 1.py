import sys
from collections import deque
import heapq
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

n,m,a,b,c = list(map(int,sys.stdin.readline().split()))
ways = [[] for i in range(n)]
bang = [[500000*20+1 for i in range(21)] for i in range(n)]
hq = [0]
fh = {}
hqis = [False for i in range(500000*20+1)]
fh[0] = deque([(a-1,0)])
bang[a-1][0]=0
for i in range(m):
    d = list(map(int,sys.stdin.readline().split()))
    ways[d[0]-1]+=[[d[1]-1,d[2]]]
    ways[d[1]-1]+=[[d[0]-1,d[2]]]

while hq:
    #print(hq)
    qpopn = heapq.heappop(hq)
    hqis[qpopn]=False
    qpoplen = len(fh[qpopn])
    for _ in range(qpoplen):
        qpop = fh[qpopn].popleft()
        if(qpopn == bang[qpop[0]][qpop[1]]):
            for i in ways[qpop[0]]:
                dum = (qpopn+i[1],i[0],max(qpop[1],i[1]))
                if(bang[i[0]][dum[2]] > dum[0] and dum[0] <= c):
                    if(hqis[dum[0]]==False):
                        heapq.heappush(hq,dum[0])
                        hqis[dum[0]] = True
                    if(dum[0] not in fh):fh[dum[0]]=deque()
                    fh[dum[0]].append((dum[1],dum[2]))
                    bang[i[0]][dum[2]]=dum[0]
r = -1  
for i in range(21):
    if (bang[b-1][i] != 500000*20+1):
        r = i
        break
print(r)
