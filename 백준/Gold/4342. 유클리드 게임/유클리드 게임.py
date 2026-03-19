def sol(a,b):
    
    if(b<a): a,b=b,a
    if(b%a==0):return 1
    if(a*2 <= b):
        return 1
    else:
        return 1-sol(a,b-a)
while 1:
    a,b = sorted(list(map(int,input().split())))
    if(b==0):break
    print("BA"[sol(a,b)]+" wins")