import sys
#from collections import deque
a = int(input())
li2 = list(map(int,input().split()))
b = int(input())
def add(q):
    re = 0
    for i in range(a):
        re+=min(li2[i],q)
    return re
c = 1
d = max(li2)
t = -1
if(add(d) <= b):
    t = d
else:
    while 1:
        e = c+(d-c)//2
        if(add(e) > b):
            d = e
        else:
            c = e
        if((d-c) == 1):
            break
    t = c
            
print(t)