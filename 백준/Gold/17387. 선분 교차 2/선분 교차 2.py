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

a,b,c,d=list(map(int,sys.stdin.readline().split()))
li = [[a,b],[c,d]]
a,b,c,d=list(map(int,sys.stdin.readline().split()))
li2 = [[a,b],[c,d]]

def sol2(li,x):
    div = (li[0][0]-li[1][0])
    li2_s = li[0][1]*div+(x-li[0][0])*((li[0][1]-li[1][1]))

    return li2_s,div

def sol3(a,b):
    a.sort()
    b.sort()
    if(a[0]>b[0]):a,b=b,a
    if(a[1] < b[0]):return 0
    return 1

def sol4(a,b,c):
    if (min(a,b) <= c <= max(a,b)):return 1
    return 0

def sol(li,li2):
    li.sort()
    li2.sort()
    div = (li[0][0]-li[1][0])
    div2 = (li2[0][0]-li2[1][0])

    if(div==0 or div2==0):
        if(div==0 and div2==0):
            if(li[0][0]==li2[0][0]):
                #print(max(li[0][1],li[1][1]))
                if(li[0][1] > li2[0][1]):
                    li,li2=li2,li
                if(max(li[0][1],li[1][1]) < min(li2[0][1],li2[1][1])):
                    return 0
            else:
                return 0
        else:
            if(div2==0): li,li2=li2,li

            li1_s,div = sol2(li2,li[0][0])

            if not (sol4(li2[0][0],li2[1][0],li[0][0])):
                return 0
            if not (sol4(li[0][1]*div,li[1][1]*div,li1_s)):
                return 0
    else:
        li2_s,div = sol2(li,li2[0][0])
        li2_e,div = sol2(li,li2[1][0])

        li1_s,div2 = sol2(li2,li[0][0])
        li1_e,div2 = sol2(li2,li[1][0])

        s = li2_s-li2[0][1]*div
        e = li2_e-li2[1][1]*div

        if(sol3([li[0][0],li[1][0]],[li2[0][0],li2[1][0]])==0):
            return 0

        if(min(s,e) <= 0 and max(s,e) >= 0):
            pass
        else:
            return 0

        s = li1_s-li[0][1]*div2
        e = li1_e-li[1][1]*div2

        if(min(s,e) <= 0 and max(s,e) >= 0):
            pass
        else:
            #print(s,e)
            return 0
    return 1

if(sol(li,li2)!=sol(li,li2)):
    print(0/0)
else:
    print(sol(li,li2))