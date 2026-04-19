import sys
#from collections import deque
d = list(map(int,input().split()))
li = [[0,0],[0,0],[0,0]]
li[0][0],li[0][1] = map(int,input().split())
li[1][0],li[1][1] = map(int,input().split())
li[2][0],li[2][1] = map(int,input().split())
t= 0
s= 0
for i in range(max(li[0][1],li[1][1],li[2][1])+1):
    for j in range(3):
        if(li[j][0] == i):
            t+=1
        if(li[j][1] == i):
            t-=1
    if(t):s+=d[t-1]*t
print(s)