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
rr = 0
for i in range(2023,li[0]+1):
    yun =0
    if(i%100!=0 and i%4==0):
        yun = 1
    if(i%400==0):
        yun=1
    days = [0,31,28+yun,31,30,31,30,31,31,30,31,30,31]
    maxs = 13
    if(i==li[0]):
        maxs = li[1]+1
    for j in range(1,maxs):
        maxs2 = days[j]+1
        if(i==li[0] and j==li[1]):
            maxs2 = li[2]+1
        for k in range(1,maxs2):
            if((str(i)+str(j)+str(k)).count('1') >= n):
                rr+=1

print(rr)