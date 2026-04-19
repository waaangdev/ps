n = int(input())
dum = 1
dum2 = 3
r = 0
while dum <= n:
    r+=1
    dum+=dum2
    dum2+=2
print(r)