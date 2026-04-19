n = int(input())
r,i = 0,1
p = n+1
while(p > i):
    dum = (n+i-1)//(i)
    r+=dum*(dum != i)
    r+=i*(p-dum)
    p = dum
    i+=1
print(r)