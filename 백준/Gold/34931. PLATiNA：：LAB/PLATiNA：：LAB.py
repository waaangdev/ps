import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n,t = list(map(int,sys.stdin.readline().split()))
li = sys.stdin.readline().strip()
li2 = [0 for i in range(n+2)]
li = li[0]+li+li[-1]
c = 0
st = 0
for i in range(n+1):
    if(li[i] != li[i+1]):
        c=1
    else:
        if(c != 0):
            dum = 1
            l,r = st+1,i-1
            while l<=r:
                li2[l] = min(t,dum)
                li2[r] = min(t,dum)
                l+=1
                r-=1
                dum+=1

        st = i+1
        c = 0
#print(li2)
li = list(li)
for i in range(n+2):
    if(li2[i]%2==1):
        if(li[i]=="A"):li[i]="B"
        else:li[i]="A"
li=''.join(li)
print(li[1:-1])