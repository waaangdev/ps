import sys
from collections import deque

a,b = map(int,sys.stdin.readline().split())

li = [i for i in range(a)]

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
r = 0
for i in range(b):
    c,d = map(int,sys.stdin.readline().split())
    
    if(find(c) == find(d)):
        r = i+1
        break
    #print(find(6),find(3))
    li[find(c)],li[find(d)] = union(c,d)
    #print(li)
        
print(r)