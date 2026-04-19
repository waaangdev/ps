import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for i in range(n)]
li2 = (sorted([(li[i],i) for i in range(n)]))[::-1]
li3 = [0 for i in range(n)]
sea = 1
hhis = li2[0][0]
rr = 2
ls = 0
rs = 0
for i in li2:
    if(hhis!=i[0]):
        rr = max(rr,sea+ls+rs)
    hhis= i[0]
    l = (i[1]-1 == -1 or li3[i[1]-1])*1
    r = (i[1]+1 == n or li3[(i[1]+1)%n])*1

    li3[i[1]] = 1
    if(i[1] == 0):
        ls = 1
    if(i[1] == n-1):
        rs = 1

    if(not l and not r):
        sea+=1
    elif(l and r):
        sea-=1
    #print("sea",sea,ls,rs,i[0])
rr = max(rr,sea+ls+rs)

print(rr-1)