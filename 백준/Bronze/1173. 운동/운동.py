import sys
a,b,c,d,e = map(int,input().split())
t = 0
m = b
u = 0
if(b+d > c):
    print(-1)
else:
    while 1:
        t+=1
        if(m+d <= c):
            m+=d
            a-=1
        else:
            m = max(b,m-e)
        if(not a):
            print(t)
            break