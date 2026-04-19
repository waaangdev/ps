#캡사이신

import sys
n = int(input())
li2 = list(map(int,sys.stdin.readline().strip().split()))
li = sorted(li2)

pows = [0 for i in range(300000)]
pows[0] = 1
pows[1] = 2
for i in range(2,300000):
    pows[i] = pows[i//2]**2*(i%2+1)%1000000007

dum = 0
# for i in range(n-1):
#     dum += (li[i+1] - li[i])
#     dum %= 1000000007
r = 0
dp = [0 for i in range(300001)]
p1,p2 = 0,n-1
for i in range(2,n+1):
    rdum = 0
    rdum2 = 0
    #if(i>2):
    #    rdum2+= ((dp[i-1])-((li[i-2]-li[0])+(li[n-1]-li[n-1-(i-2)]))*(pows[i-3]))*(pows[i-3])
    dum+=(li[p2]-li[p1])
    dum %= 1000000007
    p2-=1
    p1+=1
    rdum= (dum)*(pows[i-2])
    # if(i>2 and i < n):
    #     rdum+= (dum)*(pows[i-2])
    #     #print((dum+dum-((li[1]-li[0])+(li[n-1]-li[n-2]))))
    # else:
    #     rdum+= (dum)*(pows[i-2])

    #print(rdum)
    #rdum += rdum2
    #dp[i] = rdum
    r+=rdum
    r%= 1000000007
print(r)