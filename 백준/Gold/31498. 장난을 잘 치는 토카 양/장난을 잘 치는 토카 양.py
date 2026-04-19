import sys
# from collections import deque
# import heapq
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


a,b = list(map(int,sys.stdin.readline().split()))
c,d = list(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline())

if(k==0):
    dum = a//b
    if(b*dum < a):
        dum+=1
    if(d*dum >= a+c):
        print(-1)
    else:
        print(dum)
else:
    n = b//k
    fx = lambda x: b*x-(x)*(x-1)//2*k
    dum = fx(n)

    if(dum >= a):
        l,r = 0,n+1
        while(l+1!=r):
            mid = (l+r)//2
            dum = fx(mid)
            #print(dum)
            if(dum > a):
                r = mid
            else:
                l=mid
        #print(l)
        if(fx(l) < a):
            l+=1
        
        if(d*l >= a+c):
            print(-1)
        else:
            print(l)

    else:
        print(-1)