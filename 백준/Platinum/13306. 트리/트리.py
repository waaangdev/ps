import sys
sys.setrecursionlimit(200001)
from collections import deque
n,q = list(map(int,sys.stdin.readline().strip().split()))
par = [0 for i in range(n)]
unionfind = [i for i in range(n)]

def Find(a):
    if(unionfind[a]==a): return a
    dum = Find(unionfind[a])
    unionfind[a] = dum
    return dum

def Union(a,b):#a<b
    if(a==b):return
    if(a>b):Union(b,a)
    unionfind[Find(b)] = Find(a)


for i in range(n-1):
    par[i+1]=int(sys.stdin.readline())-1
inps = []
for i in range(n-1+q):
    inpli = list(map(int,sys.stdin.readline().strip().split()))
    if(inpli[0] == 0):
        inps.append([0,inpli[1]-1,par[inpli[1]-1]])
        par[inpli[1]-1] = -1
    else:
        inps.append([1,inpli[1]-1,inpli[2]-1])
inps.reverse()

rl = []
# for i in range(n):
#     if(par[i]!=-1):Union(i,par[i])
for i in inps:
    if(i[0]==0):Union(i[1],i[2])
    else:
        if(Find(i[1])==Find(i[2])):
            rl.append("YES")
        else:
            rl.append("NO")
    #print(unionfind)
rl.reverse()
print('\n'.join(rl))