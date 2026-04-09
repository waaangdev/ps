m=int(input())
n=int(input())
r = 0
r2 = n
for i in range(m,n+1):
    if(i<2):continue
    d = 1
    for j in range(2,i//2+1):
        if(i%j==0):
            d=0
    if(i==2):d=1
    if(d):
        r+=i
        r2=min(r2,i)
if(r==0):
    print(-1)
else:
    print(r)
    print(r2)