import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

#sys.setrecursionlimit(100001)

# for i in range(int(sys.stdin.readline())):

n =  int(sys.stdin.readline())
k =  int(sys.stdin.readline())

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i*j,end=' ')
#     print()

l,r = 1,n**2+1
while (l+1!=r):
    mid = (l+r)//2

    dum = 0
    dum_l = 0
    dum2 = 0
    for i in range(1,n+1):
        dum+=min(n,mid//i)
        if(mid%i==0 and mid//i <= n):
            dum_l -= dum2
            dum2=1
    dum_l+=dum
    
    #print(mid,dum,dum_l,dum2)
    if(dum_l > k):
        r = mid
    elif(dum < k):
        l = mid
    else:
        if(dum2 == 0):
            r = mid
        else:
            l = mid
            break
print(l)