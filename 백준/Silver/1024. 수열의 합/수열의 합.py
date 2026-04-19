import sys
n,m = map(int,sys.stdin.readline().split())
d = 0
for i in range(m,101):
    n2 = n//i
    if(n//i-(i-i//2-1) <0):continue
    dum = [n2-j for j in range(i-i//2)][::-1]+[n2+j+1 for j in range(i//2)]
    if(sum(dum)==n):
        print(*dum)
        d = 1
        break
if(d==0):print(-1)