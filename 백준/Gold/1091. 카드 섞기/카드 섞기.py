import sys
#from collections import deque
n = int(input())
h = list(map(int,input().split()))
s = list(map(int,input().split()))
c = [i for i in range(n)]
c1 = [i for i in range(n)]
ch = 0
while 1:
    br = 1
    for i in range(n):
        if(i%3 != h[c[i]]):
            br = 0
    if(br): break
    for i in range(n):
        c1[s[i]] = c[i]
    c = list(c1)
    ch +=1
    if(c == list(range(n))):
        ch = -1
        break
print(ch)