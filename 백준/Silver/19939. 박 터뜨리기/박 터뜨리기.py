import sys
a,b = list(map(int,sys.stdin.readline().strip().split()))

dum = (b-1)*b/2

dum+=b

a-=dum

if(a<0):
    print(-1)
else:
    a= a%b

    if(a==0):
        print((b-1))
    else:
        print((b))