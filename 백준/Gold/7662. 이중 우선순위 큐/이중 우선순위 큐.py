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

for _ in range(int(sys.stdin.readline())):
    cnt = 0
    li1 = []
    li12 = []
    li2 =[]
    li22 =[]
    n = int(sys.stdin.readline())
    for _ in range(n):
        inp = sys.stdin.readline().strip().split()

        if(inp[0]=='I'):
            inp[1]=int(inp[1])
            heapq.heappush(li1,inp[1])
            heapq.heappush(li2,-inp[1])
            cnt+=1

        else:
            if(cnt!=0):
                cnt-=1
                if(inp[1]=='-1'):
                    heapq.heappush(li22,-heapq.heappop(li1))
                else:
                    heapq.heappush(li12,-heapq.heappop(li2))
        while(li1 and li12 and li1[0]==li12[0]):
            heapq.heappop(li1)
            heapq.heappop(li12)
        while(li2 and li22 and li2[0]==li22[0]):
            heapq.heappop(li2)
            heapq.heappop(li22)
    if(cnt==0):
        print("EMPTY")
    else:
        print(-heapq.heappop(li2),heapq.heappop(li1))