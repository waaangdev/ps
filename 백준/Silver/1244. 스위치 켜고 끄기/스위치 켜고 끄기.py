n = int(input())
li = list(map(int,input().split()))
m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    if(a==1):
        for i in range(b-1,n,b):
            li[i] = 1-li[i]
    else:
        b-=1
        p1,p2 = b,b
        li[b] = 1-li[b]
        while(li[p1] == li[p2]):
            li[p1] = 1-li[p1]
            li[p2] = 1-li[p2]
            p1+=1
            p2-=1
            if(p1==n or p2==-1):
                break
    #print(*li)
for i in range(n//20+(n%20!=0)):
    print(*li[i*20:min(n,i*20+20)])