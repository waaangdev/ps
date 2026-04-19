import sys
from collections import deque
import heapq
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
n,m,k = list(map(int,sys.stdin.readline().split()))
def sol(li,x):
    #print(li,x)
    li2 = [[],[],[]]
    if(len(li)<=k):return (0,"")
    if(x == m):return (100,"")
    for i in li:
        if(i[x]=="R"):li2[0]+=[i]
        if(i[x]=="S"):li2[1]+=[i]
        if(i[x]=="P"):li2[2]+=[i]
    r = 100
    r2 = ""
    for i in range(3):
        if(len(li2[i])):
            dum = sol(li2[i],x+1)
            if(r>dum[0]):
                r = dum[0]
                r2 = "SPR"[i]+dum[1]
    return (r+1,r2)
li = []
for i in range(n):
    li.append(sys.stdin.readline().strip())
r = (sol(li,0))
if(r[0]>=100):
    print(-1)
else:
    print(r[0])
    print(r[1])