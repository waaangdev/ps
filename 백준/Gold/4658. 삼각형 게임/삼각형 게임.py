import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

t2 = [1,2,4,8,16,32,64]
li = []
li2 =[]
li3 = [0 for i in range(101)]
dp = [[[-2 for i in range(64)] for i in range(18)] for i in range(18)]
def sol(bi,num,st):
    if(dp[num][st][bi] !=-2):return dp[num][st][bi]
    if(bi==63):
        if(num==st):return 0
        else:return -1
    r = -1
    dum = st
    for i in range(6):
        for j in range(3):
            if(bi%t2[i+1]<t2[i] and (num == li3[li[i][j]] or bi==0)):
                if(bi==0):dum = li3[li[i][j]]
                a = sol(bi+t2[i],li3[li[i][(j+2)%3]],dum)
                #print(1)
                if(a!=-1):
                    r=max(r,a+li[i][(j+1)%3])
    dp[num][st][bi] = r
    return r

while 1:
    li = []
    li2 = []
    li3 = [0 for i in range(101)]
    dp = [[[-2 for i in range(64)] for i in range(18)] for i in range(18)]
    for i in range(6):
        li1 = list(map(int,sys.stdin.readline().split()))
        li.append(li1[:])
        li2+=li1[:]
    li2.sort()
    for i in range(len(li2)):
        li3[li2[i]]=i
    r = sol(0,0,0)
    if(r==-1):print("none")
    else:print(r)
    #print(dp)
    if(sys.stdin.readline().strip() == "$"):break