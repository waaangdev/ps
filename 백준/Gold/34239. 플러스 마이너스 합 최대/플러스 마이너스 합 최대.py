import sys
n = int(input())
li =list(map(int,sys.stdin.readline().strip().split()))
# -1 -3 -7 -5 -2
dum = 0
mins = 0
r = -1000000000000000000
for i in range(n):
    dum+=li[i]*(-(i%2*2)+1)
    r = max(r,(dum-mins))
    #print(mins,dum)
    if(i%2==1):mins = min(mins,dum)

dum = 0
mins = 1000000000000000000
for i in range(n):
    dum+=-li[i]*(-(i%2*2)+1)
    if(i>0):r = max(r,(dum-mins))
    #print(mins,dum)
    if(i%2==0):mins = min(mins,dum)
print(r)