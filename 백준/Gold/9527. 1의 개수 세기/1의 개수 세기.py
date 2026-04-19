def sol(num):
    dum = 2
    r = 0
    while (1):
        dum2 = num//dum
        r2 = 0
        r2+=dum2*(dum//2)

        if(num%(dum) >= (dum//2)):
            r2+=num%(dum)-(dum//2)+1
        
        r += r2
        if(dum2 == 0):break

        dum*=2
    return r

a,b = map(int,input().split())
print(sol(b)-sol(a-1))