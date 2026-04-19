import sys
from collections import deque
n,k = map(int,input().split())
li = deque(list(map(int,input().split())))
ro = deque([0 for i in range(n)])
br = 0
dan = 0
while 1:
    dan+=1
    li.insert(0,li.pop())
    ro.pop()
    ro.insert(0,0)
    for i in range(1,len(ro)+1):
        if(ro[len(ro)-i] == 1):
            if(i == 1):
                ro[len(ro)-i] = 0
            elif(li[len(ro)-i+1] > 0 and ro[len(ro)-i+1] == 0):
                ro[len(ro)-i] = 0
                ro[len(ro)-i+1] = 1
                li[len(ro)-i+1] -= 1
                if(li[len(ro)-i+1] == 0):
                    br+=1
    ro[n-1] = 0
    if(li[0] > 0):
        li[0] -= 1
        ro[0] = 1
        if(li[0] == 0):
            br+=1
    if(br >= k):
        break
print(dan)