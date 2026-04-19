import sys
n,m= map(int,sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(n)]
li.sort()
r = 2000000000
p = 0
for i in li:
    while(li[p] < i+m):
        p+=1
        if(p==n):break
    if(p==n):break
    r = min(r,li[p]-i)
print(r)