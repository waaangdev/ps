r =-1
n =int(input())
for i in range(n):
    dum = sum(list(map(int,input().split())))
    if dum >= 512:
        if r == -1:
            r = dum
        r = min(r,dum)
print(r)