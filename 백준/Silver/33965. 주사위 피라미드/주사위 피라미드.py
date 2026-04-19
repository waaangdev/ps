#주사위 피라미드
import sys

n = int(input())
dp = [0 for i in range(n)]
dp2 = [0 for i in range(n)]

li = [6,11,15,18,20]
li2 = [1,3,6,10,15]

dp[0] =20
dp2[0] = 15
dum = 2 #4개
dum2 = 0 #3개
dum3 = 1 #2개
dum4 = 0 #1개
for i in range(1,n):
    dp[i] += dp[i-1]
    dp[i] += dum*li[3]
    dp[i] += dum2*li[2]
    dp[i] += dum3*li[1]
    dp[i] += dum4*li[0]

    dp2[i] += dp2[i-1]
    dp2[i] += dum*li2[3]
    dp2[i] += dum2*li2[2]
    dp2[i] += dum3*li2[1]
    dp2[i] += dum4*li2[0]

    dum = 2
    dum2 += 1
    dum3 = 1
    dum4 += 2

print(dp[n-1]+dp2[n-1])
