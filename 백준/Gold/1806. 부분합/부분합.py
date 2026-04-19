import sys
#from collections import deque

#부분합

a,b = map(int,input().split())
li = list(map(int,sys.stdin.readline().strip().split()))

r = 0
s,e = 0,0
r2 = li[0]

while 1:
    if(e == a):
        break
    
    if(r2 >= b):
        if(e-s == 0):
            r= 1
            break
        else:
            r= min(r,e-s+1)
            if(r == 0): r = e-s+1

            r2 -= li[s]
            s+=1
    else:
        e+=1
        if(e == a):
            break
        r2 += li[e]
print(r)