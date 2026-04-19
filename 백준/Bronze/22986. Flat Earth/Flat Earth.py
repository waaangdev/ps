for i in range(int(input())):
    a,b = map(int,input().split())
    c=max(0,a-b-1)
    print((a*(a+1))*2-(c*(c+1))*2)