input()
n = list(reversed(sorted(list(map(int,input().split())))))
if(n[0] >1440):
    t = 1441
else:
    t = 0
    while 1:
        if(n[0] > 0):n[0] -= 1
        else:break
        if(len(n) != 1):
            if(n[1] > 0):n[1] -= 1
        t+=1
        n = list(reversed(sorted(n)))
if (t > 1440):
    print(-1)
else:
    print(t)