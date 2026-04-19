import sys
sys.setrecursionlimit(100010)

n=int(input())
dp=[[-1]*3 for _ in range(n)]
ways=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(lambda x:int(x)-1,input().split())
    ways[a]+=[b]
    ways[b]+=[a]
def sol(idx,num,his):
    if(dp[idx][num]==-1):
        r = 1
        for i in ways[idx]:
            if(i!=his):r+=sol(i,1,idx)
        dp[idx][num]=r
        if(num != 0):
            r2=0
            for i in ways[idx]:
                if(i!=his):r2+=sol(i,num-1,idx)
            dp[idx][num]=min(r,r2)
    return dp[idx][num]
print(sol(0,1,-1))