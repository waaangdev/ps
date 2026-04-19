import sys
from collections import deque

def find(x):
    if(li[x] == x):
        return x
    else:
        dum = x
        while 1:
            dum = li[dum]
            if(li[dum] == dum):
                return dum
            
def union(x,y):
    x = find(x)
    y = find(y)
    
    if(x < y):
        y = x
    else:
        x = y
    return x,y

a,b = map(int,sys.stdin.readline().split())
li = {}
li2 = []

for i in range(a):
    inp = sys.stdin.readline().split()
    li[inp[2]] = inp[2]
    li2.append(inp[2])


for i in range(b):
    inp = sys.stdin.readline().split()
    
    c = inp[2].split(',')[0]
    d = inp[4].split(',')[0]    
    w = inp[4].split(',')[1]
    
    
    if(find(c) != find(d)):
        if(w == '1'):
            li[find(d)] = li[find(c)]
        else:
            li[find(c)] = li[find(d)]
    else:
        if(w == '1' and find(c) != c):
            li[find(d)] = c
            li[c] = c
        elif(w == '2' and find(d) != d):
            li[find(c)] = d
            li[d] = d
r = 0
r1 = []
for i in li2:
    if(li[i] == i):
        r+=1
        r1.append(i)

print(r)
r1.sort()
for i in range(r):
    print("Kingdom of "+r1[i])