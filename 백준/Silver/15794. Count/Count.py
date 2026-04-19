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
k = int(sys.stdin.readline())
li2 = [0]*20002
for i in li:
    li2[i+10000]+=1

mins = 200001
mini = 0
for i in range(-10000,10001):
    for j in range(i+1,10001):
        if(li2[i+10000]*li2[j+10000]!=0):
            if(abs((i+j)-k)==mins):
                mini+=li2[i+10000]*li2[j+10000]
            if(abs((i+j)-k)<mins):
                mini=li2[i+10000]*li2[j+10000]
                mins=abs((i+j)-k)
for i in range(-10000,10001):
    if(li2[i+10000]>1):
        if(abs((i+i)-k)==mins):
            mini+=li2[i+10000]*(li2[i+10000]-1)//2
        if(abs((i+i)-k)<mins):
            mini=li2[i+10000]*(li2[i+10000]-1)//2
            mins=abs((i+i)-k)
print(mini)