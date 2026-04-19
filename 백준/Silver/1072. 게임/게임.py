import sys
#from collections import deque
a,b = map(int,input().split())
def add(q):
    re = int((b+q)*100//(a+q))
    return re
c = 1
d = a+1
t = -1
if(a == b):
    t = -1
elif(add(1) != add(0)):
    t = 1
else:
    while 1:
        e = c+(d-c)//2
        if(add(e) > add(0)):
            d = e
        else:
            c = e
        if((d-c) == 1):
            break
    t = d
    if(t == a+1):
        t = -1
print(t)