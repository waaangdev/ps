a = int(input())
li = []
for i in range(a):
    li.append(list(map(int,input().split())))
dp = [[[1001,1001,1001] for i in range(a)] for i in range(3)]
r = 1000*1001
for j in range(3):
    dp[j][0][j]=li[0][j]
    for i in range(1,a):
        dp[j][i][0] = min(dp[j][i-1][1],dp[j][i-1][2])+li[i][0]
        dp[j][i][1] = min(dp[j][i-1][0],dp[j][i-1][2])+li[i][1]
        dp[j][i][2] = min(dp[j][i-1][1],dp[j][i-1][0])+li[i][2]
    for i in range(3):
        if(i!=j):
            r = min(r,dp[j][a-1][i])
print(r)