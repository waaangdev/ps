dp=[0]*1000001
a,b=map(int,input().split())
for i in range(a+1,b+1):
    dp[i]=dp[i-1]
    if(i%2==0 and i//2 >= a):
        dp[i]=min(dp[i],dp[i//2])
    dp[i]+=1
print(dp[b])