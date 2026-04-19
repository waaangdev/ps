import sys
a,b = map(int,input().split())

bl1 = [i+1 for i in range(b//2)]+[1000000000-i for i in range(b-b//2)]
dum = sum(bl1)//b
al1 = [dum+2+i for i in range(a)]

if(max(al1) > 1000000000-(b-b//2)):
    al1 = [i+1 for i in range(a-a//2)]+[1000000000-i for i in range(a//2)]
    dum = sum(al1)//a
    bl1 = [dum-2-i for i in range(b)]

    if((a//2)*b > (a-a//2)*b or min(bl1) < 1):
        print(-1)
    else:
        print(*al1)
        print(*bl1)

else:
    print(*al1)
    print(*bl1)

# print(sum(bl1)/b,"<",sum(al1)/a,(b//2)*a,"<=",(b-b//2)*a)
# print(*al1)
# print(*bl1)