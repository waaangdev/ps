n,k = map(int,input().split())
li = [1 for i in range(n)]
idx = 0
rl = []
for i in range(n):
    dum = 0
    while 1:
        if(li[idx]):
            dum+=1
        if(dum==k):break
        idx+=1
        idx = idx%n

    rl.append(idx+1)
    li[idx]=0
print("<"+', '.join(map(str,rl))+">")
