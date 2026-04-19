a = int(input())
for _ in range(a):
    c,d = map(int,input().split())
    c2 = 1
    for i in range(d):
        c2*=c
        c2 %= 10
    if(c2==0):
        print(10)
    else:
        print(c2)
    