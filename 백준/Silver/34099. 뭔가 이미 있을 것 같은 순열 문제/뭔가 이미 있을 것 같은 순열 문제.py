

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    if(k == 1):
        li = []
        p1 = 1
        p2 = (n+1)//2+1
        for i in range(n):
            if(i%2==0):
                li.append(p1)
                p1+=1
            else:
                li.append(p2)
                p2+=1
        r = 1
        for i in range(n-1):
            if(abs(li[i]-li[i+1])==1): r=0
        if(r==0):
            li = []
            p1 = 1
            p2 = (n)//2+1
            for i in range(n):
                if(i%2):
                    li.append(p1)
                    p1+=1
                else:
                    li.append(p2)
                    p2+=1
            r = 1
            for i in range(n-1):
                if(abs(li[i]-li[i+1])==1): r=0

            if(r==0):
                print(-1)
            else:
                print(*li)
        else:
            print(*li)
    else:
        print(*[i+1 for i in range(n)])