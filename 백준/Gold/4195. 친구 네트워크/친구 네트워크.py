import sys
from collections import deque

def find(x):
    if(li[x] == x):
        return x
    else:
        li[x]=find(li[x])
        return li[x]
            
def union(x,y):
    x = find(x)
    y = find(y)
    
    if(x < y):
        li[y]=x
    else:
        li[x]=y

a = int(sys.stdin.readline())

for _ in range(a):
    b = int(sys.stdin.readline())

    li = {}
    li2 = {}


    for i in range(b):
        c,d = sys.stdin.readline().split()
        if(c not in li):
            li[c] = c
            li2[c] = 1
        if(d not in li):
            li[d] = d
            li2[d] = 1
        if(find(c) != find(d)):
            if(find(c) < find(d)):
                li2[find(c)] += li2[find(d)]
                print(li2[find(c)])
            else:
                li2[find(d)] += li2[find(c)]
                print(li2[find(d)])
            union(c,d)
        else:
            print(li2[find(c)])
            
