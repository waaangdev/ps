import sys

sys.setrecursionlimit(1000001)

a=int(input())
way = [[] for i in range(a)]
for i in range(a-1):
    d1,d2 = map(int,sys.stdin.readline().split())
    d1-=1
    d2-=1
    way[d1].append(d2)
    way[d2].append(d1)
dp = [0]*a

def sol(idx):
    dp[idx]=1
    r = [1,0]#본인1,나머지1
    for i in way[idx]:
        if(dp[i]==0):
            dum = sol(i)
            r[0]+=min(dum)
            r[1]+=dum[0]
    return r

print(min(sol(0)))