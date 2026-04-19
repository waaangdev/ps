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

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

lis = [li[::2],li[1::2]]
#print(lis)
rl = []
idx = 0
for li1 in lis:
    p,m = 0,0
    for i in range(len(li1)):
        li1[i]+=-p+m
        #print(li1)
        if(li1[i] != 0):
            rl.append([idx+i*2+1,abs(li1[i]),[1,3][li1[i]>0]])
            if(li1[i]>0):
                p+=abs(li1[i])
            else:
                m+=abs(li1[i])
        p,m=m,p

    idx = 1
print(len(rl))
for i in rl:
    print(*i)