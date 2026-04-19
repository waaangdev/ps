while 1:
    a,b=list(map(int,input().split()))
    if(a==b and a==0):break
    dum=0
    while dum**b <= a:
        dum+=1
    if dum==0:
        print(0)
    else:
        if abs(dum**b-a) < abs((dum-1)**b-a):
            print(dum)
        else:
            print(dum-1)