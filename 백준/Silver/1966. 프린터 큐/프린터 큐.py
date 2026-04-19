import sys
from collections import deque
a = int(input())
for _ in range(a):
    b,c = map(int,sys.stdin.readline().split())
    li = list(map(int,sys.stdin.readline().split()))
    li2 = sorted(li)[::-1]
    li = deque([[li[i],i] for i in range(len(li))])
    t = 0
    while 1:
        d = li.popleft()
        if(d[0] == li2[0]):
            t+=1
            del li2[0]
            if(d[1] == c):
                print(t)
                break
        else:
            li.append(d)