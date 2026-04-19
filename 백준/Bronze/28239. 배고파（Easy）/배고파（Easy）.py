a=int(input())
for i in range(a):
    b = int(input())
    b2 = (bin(b)[::-1])
    if(b2.count('1')==1):
        dum=b2.index('1')
        print(dum-1,dum-1)
    else:
        dum=b2.index('1')
        dum2=b2.index('1',dum+1)
        print(dum,dum2)