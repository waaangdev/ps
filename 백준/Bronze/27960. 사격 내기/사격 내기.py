a,b = map(int,input().split())
c = 512
r = 0
for i in range(10):
    d = 0
    if(a-c >= 0):
        a-=c
        d +=1
    if(b-c >= 0):
        b-=c
        d +=1
    if(d == 1):
        r+=c
    c = c/2
print(round(r))