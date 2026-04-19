a = int(input())
for i in range(a):
    b,c,d = map(int,input().split())
    li = list(map(lambda x: int(x)*(int(x)!=-1)+1500*(int(x)==-1),input().split()))
    dum = d
    dum = max(dum,c-min(li))
    if(dum!=1):
        print("The scoreboard has been frozen with",dum,"minutes remaining.")
    else:
        print("The scoreboard has been frozen with 1 minute remaining.")