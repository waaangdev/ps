import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

li.sort()

if(n == 1):
    print(li[0])
elif(n == 3):
    print(li[-2])
    print(*li)
else:
    print(li[-2])
    l,r = 0,n-3
    for i in range((n-3)//2):
        print(li[l],li[(l+r)//2],li[r])
        l+=1
        r-=1
    print(li[(l+r)//2],li[-2],li[-1])