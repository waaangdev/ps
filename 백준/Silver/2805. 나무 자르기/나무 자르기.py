import sys
#from collections import deque
a,b = map(int,input().split())
li2 = list(map(int,input().split()))
def add(q):
    re = 0
    for i in range(a):
        if(li2[i] > q):
            re+=li2[i]-q
    return re
c = 0
d = max(li2)
t = -1
if(add(c) == b):
    t = c
elif(add(d) == b):
    t = c
else:
    while 1:
        e = c+(d-c)//2
        if(add(e) == b):
            t = e
            break
        elif(add(e) < b):
            d = e
        else:
            c = e
        if((d-c) == 1):
            break
    if(t == -1):
        t = c
            
print(t)