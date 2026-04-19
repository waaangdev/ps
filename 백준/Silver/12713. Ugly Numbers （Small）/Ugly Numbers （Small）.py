import sys
n = int(input())
inp = ""

dp = [[[[[-1,0] for i in range(14)] for j in range(2)] for k in range(211)] for l in range(14)]
bang = 0

def req(idx,sums,mode,modei):
    sums %= 210
    if(idx == len(inp)):
        sums = sums+int(inp[modei:idx])*mode
        sums = abs(sums)
        return 0+1*(sums%2==0 or sums%3==0 or sums%5==0 or sums%7==0)
    if(dp[idx][sums][0+1*(mode==1)][modei][1] == bang):
        return dp[idx][sums][0+1*(mode==1)][modei][0]
    
    r = 0
    r+=req(idx+1,sums,mode,modei)
    r+=req(idx+1,sums+int(inp[modei:idx])*mode,1,idx)
    r+=req(idx+1,sums+int(inp[modei:idx])*mode,-1,idx)

    dp[idx][sums][0+1*(mode==1)][modei] = [r,bang]
    return r

for i in range(n):
    inp = input()
    bang += 1
    r = req(1,0,1,0)

    print(F"Case #{i+1}: {r}")