import sys

li = []

def sol(idx,d,num):
    #print(idx,d,num)
    if(d==1):
        return li[idx]
    if(idx < num//2):
        return sol(idx,d-1,num//2)
    if(idx == num//2):
        return sol(idx-1,d-1,num//2)
    return sol(idx-1-num//2,d-1,num//2)

li,n =input().split()
n = int(n)
lli = len(li)
dum = lli
dum2 = 1
while (dum < n):
    dum*=2
    dum2 += 1

#print(n-1,dum2,dum)
print(sol(n-1,dum2,dum))