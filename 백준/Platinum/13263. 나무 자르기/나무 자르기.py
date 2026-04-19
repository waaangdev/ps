import sys
from collections import deque
import random
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

#sys.setrecursionlimit(100)

for _ in range(1):
    n = int(sys.stdin.readline())

    li = list(map(int,sys.stdin.readline().split()))
    li2 = list(map(int,sys.stdin.readline().split()))

    idx = 0

    # dp = [0 for i in range(n)]
    # for i in range(1,n):
    #     dp[i] = dp[0]+li2[0]*li[i]
    #     for j in range(0,i):
    #         dp[i] = min(dp[i],dp[j]+li2[j]*li[i])
    # print(dp)
    # dp2 = dp[:]

    dp = [0 for i in range(n)]

    def coll(a,b):
        return (dp[a]-dp[b])//(li2[b]-li2[a])+1-((dp[a]-dp[b])%(li2[b]-li2[a])==0)*1

    if(n==1):
        print(0)
    else:

        dp[1] = dp[0]+li2[0]*li[1]
        chts = [[0,0],[coll(0,1),1]]

        for i in range(2,n):
            #print(i,chts)
            l,r = 0,len(chts)
            while(l+1!=r):
                mid = (l+r)//2
                if(li[i]<chts[mid][0]):
                    r = mid
                else:
                    l = mid
            #print(chts[l][1])
            dp[i]=li[i]*li2[chts[l][1]]+dp[chts[l][1]]

            while(chts[-1][0] >= coll(i,chts[-1][1])):
                chts.pop()
            chts.append([coll(i,chts[-1][1]),i])

        
        #print(dp)
        print(dp[-1])

