a,b  = map(int,input().split())
li = list(map(int,input().split()))
p = [0,0]
t = li[0]
s = 0
while 1:
    if(t >= b):
        if(t == b):
            s+=1
        t-=li[p[0]]
        p[0]+=1
    else:
        p[1]+=1
        if(p[1] == len(li)):
            break
        t+=li[p[1]]
print(s)