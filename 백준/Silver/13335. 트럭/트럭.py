from collections import deque
a,b,c= map(int,input().split())
t = deque(list(map(int,input().split())))
r = deque([0 for i in range(b)])
ti = 0
pl = 0
while 1:
    ti += 1
    pl -= r.popleft()
    if(len(t)!= 0 and pl+t[0] <= c):
        ad = t.popleft()
        r.append(ad)
        pl+=ad
    else:
        r.append(0)
        if(pl == 0):
            break
print(ti)