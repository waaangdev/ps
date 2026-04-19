import sys
for i in range(int(input())):
    n,m,k,d = list(map(int,sys.stdin.readline().strip().split()))

    duma = ((m-1)*(m)//2)*n
    dumb = ((n-1)*(n)//2)*m*m
    duma2 = duma*k
    b = d//(duma2+dumb)
    if(b==0):
        print(-1)
    else:
        print((duma2+dumb)*b)