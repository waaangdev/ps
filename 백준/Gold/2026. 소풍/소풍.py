import sys
k,n,m = map(int,sys.stdin.readline().strip().split())
connected = [set([]) for i in range(n)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().strip().split())
    a-=1
    b-=1
    if(a>b):a,b = b,a
    connected[a].add(b)

def sol(idx,li,cnt):
    #print(idx,li,cnt)
    if(cnt == k):
        return [idx]
    if(len(li)+cnt+1 < k):
        return []
    for i in sorted(list(li)):
        dum = sol(i,(li&connected[i]),cnt+1)
        if(dum):return dum+[idx]
    return []

for i in range(n):
    dum = sol(i,connected[i],1)
    if(dum):
        dum = sorted(dum)
        print('\n'.join(list(map(lambda x:str(x+1),dum))))
        break
if(not dum):
    print(-1)