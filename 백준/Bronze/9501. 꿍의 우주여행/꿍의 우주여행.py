for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    r=0
    for I in range(a):
        c,d,e=list(map(int,input().split()))
        if(b*e <= d*c): r+=1
    print(r)