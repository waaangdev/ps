import sys
import heapq
from collections import deque
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

n,k = list(map(int,sys.stdin.readline().split()))
ways = []
for i in range(n):
    ways.append(list(map(int,sys.stdin.readline().split())))

q = deque([[k,2**k,0]])
bang = [[10000000000000000 for i in range(1024)] for i in range(10)]
while q:
    #print(q)
    qpop = q.popleft()
    for i in range(n):
        qpop2 = [i,qpop[1]|(2**i),qpop[2]+ways[qpop[0]][i]]
        if(i!=qpop[0] and bang[i][qpop2[1]] > qpop2[2]):
            q.append(qpop2)
            bang[i][qpop2[1]]=qpop2[2]
print(min([bang[i][2**n-1] for i in range(n)]))