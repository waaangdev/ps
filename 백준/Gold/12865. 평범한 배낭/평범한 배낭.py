import sys
def benang():
    for i in range(mulgun_su):
        for j in range(max_muge+1):
            if(i == 0):
                if(mulgun[i][0] <= j):
                    dp[i][j] = mulgun[i][1]
            else:
                dp[i][j] = dp[i-1][j]
                if(mulgun[i][0] <= j):
                    dp[i][j] = max(dp[i][j],mulgun[i][1]+dp[i-1][j-mulgun[i][0]])
    return dp[mulgun_su-1][max_muge]
mulgun_su,max_muge = map(int,sys.stdin.readline().split())
mulgun = []
dp = [[0 for i in range(max_muge+1)] for i in range(mulgun_su)]
for i in range(mulgun_su):
    mulgun.append(list(map(int,sys.stdin.readline().split())))
print(benang())