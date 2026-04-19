import sys
n,m = map(int,input().split())
li = list(map(int,sys.stdin.readline().strip().split()))
dum = 0
for i in range(m):
    dum+=li[i]
r = dum
for i in range(n-m):
    dum-=li[i]
    dum+=li[i+m]
    r = max(dum,r)
print(r)