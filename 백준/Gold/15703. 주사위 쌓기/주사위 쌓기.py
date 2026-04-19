import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

n = int(sys.stdin.readline())
li1 = list(map(int,sys.stdin.readline().split()))
li = [0 for i in range(1001)]
for i in range(n):
    li[li1[i]]+=1
r = 0
c = 0
while c!=n:
    left =1000
    q = deque()
    r+=1
    while (left != -1):
        br = 1
        for i in range(left,-1,-1):
            if(li[i]):
                left=i-1
                br=0
                li[i]-=1
                c+=1
                if(li[i]):q.appendleft(i)
                break

        if(br):break

        while (left != -1 and q):
            #print(left,q,c)
            if(li[left]):q.appendleft(left)

            dum = q.popleft()
            li[dum]-=1
            if(li[dum]):q.appendleft(dum)

            c+=1
            left -= 1

print(r)