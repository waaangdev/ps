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

n=int(input())
l = []
def sol2(l):
    for i in range(len(l)//2):
        if(l[-1:-2-i:-1]==l[-2-i:-3-i*2:-1]):
            return 0
    return 1
def sol(idx):
    global l
    #print(idx,l)
    if(idx==n):
        if(sol2(l)):
            print("".join(map(str,l)))

            return 1
        return 0
    l+=[1]
    if(sol2(l)):
        if(sol(idx+1)):return 1
    l[-1]=2
    if(sol2(l)):
        if(sol(idx+1)):return 1
    l[-1]=3
    if(sol2(l)):
        if(sol(idx+1)):return 1
    del l[-1]
    return 0
sol(0)