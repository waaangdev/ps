"할로윈의 양아치"

import sys
from collections import deque
poi_su,way_su,max_muge = map(int,sys.stdin.readline().split())
poi_ga = list(map(int,sys.stdin.readline().split()))
ways=[[] for i in range(poi_su)]
sys.setrecursionlimit(3005)
mulgun = []
for i in range(way_su):
    inp1,inp2 = map(int,sys.stdin.readline().split())
    ways[inp1-1].append(inp2-1)
    ways[inp2-1].append(inp1-1)
dli=[1]*poi_su
mulgun = [[] for i in range(3001)]
for i in range(poi_su):
    if(dli[i]):
        dli[i]=0
        q=deque([i])
        lll=[1,poi_ga[i]]
        while q:
            qpop=q.pop()
            for j in ways[qpop]:
                if(dli[j]):
                    q.append(j)
                    lll[0]+=1
                    lll[1]+=poi_ga[j]
                    dli[j]=0
        if(lll[0] <= 3000):
            mulgun[lll[0]].append(lll[1])
mulgunidx = []
for i in range(len(mulgun)):
    mulgun[i].sort(key = lambda x:-x)
    if(len(mulgun[i])!=0):
        mulgunidx.append(i)
#print(mulgun)
# mulgun_su = len(mulgun)
# memo = [[-1 for i in range(max_muge+1)]for i in range(mulgun_su)]
# print(benang(mulgun_su-1,max_muge))
def dps(idx,nam):
    dum=idx*(3001)+nam
    if(idx==len(mulgunidx)):return 0
    if(dp[dum]==-1):
        dp[dum]=dps(idx+1,nam)
        sums = 0
        for i in range(len(mulgun[mulgunidx[idx]])):
            sums +=mulgun[mulgunidx[idx]][i]
            dd=nam-(i+1)*(mulgunidx[idx])
            if(dd<0):break
            dp[dum]=max(dps(idx+1,dd)+sums,dp[dum])
    return dp[dum]

dp=[-1]*3001*3001
print(dps(0,max_muge-1))