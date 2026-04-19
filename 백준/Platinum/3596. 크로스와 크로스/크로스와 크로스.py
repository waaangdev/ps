dp = [-1]*2001

def sol(n):
    if(n<=0):return 0
    if(dp[n]!=-1):return dp[n]
    r = 0
    mex = [0]*(n+1)
    mex[sol(n-3)] = 1
    mex[sol(n-4)] = 1
    mex[sol(n-5)] = 1
    if(n>6):
        for i in range(3,n-3):
            mex[sol(i-2)^sol(n-i-3)] = 1
    #print(mex)
    for i in range(n+1):
        if(mex[i]):
            r = i+1
        else:
            break
    dp[n] = r
    return r

n = int(input())
if(sol(n) == 0):
    print(2)
else:
    print(1)