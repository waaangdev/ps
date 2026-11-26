import sys
from collections import deque
import random
import math
import heapq #minheap

input = lambda: sys.stdin.readline().rstrip()
print = lambda *a,end='\n': sys.stdout.write(' '.join(map(str,a))+end)

#n = int(input())
#li = list(map(int,input().split()))

sys.setrecursionlimit(100010)


n = int(input())

li = list(map(int,input().split()))
li2 = list(map(int,input().split()))

if(sorted(li) != sorted(li2)):
    print(0)
else:
    matchs = 0
    for i in range(n):
        if(li[i]==li2[i]): matchs += 1

    if(matchs == n):
        print(1)
    else:
        rr=0
        for i in range(n-1,0,-1):
            for j in range(i):
                if(li[j] > li[j+1]):
                    if(li[j]==li2[j]):matchs-=1
                    if(li[j+1]==li2[j+1]):matchs-=1
                    li[j],li[j+1] = li[j+1],li[j]
                    if(li[j]==li2[j]):matchs+=1
                    if(li[j+1]==li2[j+1]):matchs+=1
                    if(matchs == n):
                        rr=1
        print(rr)