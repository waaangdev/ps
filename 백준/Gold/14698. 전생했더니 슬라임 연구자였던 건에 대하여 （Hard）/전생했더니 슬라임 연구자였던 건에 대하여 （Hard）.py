import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li =list(map(int,sys.stdin.readline().split()))
    q = []
    for i in li:
        heapq.heappush(q,i)
    r = 1
    while(len(q)>1):
        d = heapq.heappop(q)
        d2 = heapq.heappop(q)
        d3 = d*d2
        r*=d3
        r%=1000000007
        heapq.heappush(q,d3)
    sys.stdout.write(str(r)+'\n')