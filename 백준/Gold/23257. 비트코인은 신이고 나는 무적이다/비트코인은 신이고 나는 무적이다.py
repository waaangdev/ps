

n,m= map(int,input().split())
li = list(map(abs,map(int,input().split())))

dp = [[10000 for i in range(1025)] for i in range(m+1)]

def sol(m,k):
    if(dp[m][k] != 10000):
        return dp[m][k]
    if(m==0):
        return k
    r = 0
    for i in li:
        r= max(r,sol(m-1,i)^k)
    dp[m][k] = r
    #print(m,k,r)
    return r
# for i in range(n):
#     print(bin(li[i])[2:].rjust(10,'-'))

def sol2(m,k):
    if(m==0):
        return k
    if(dp[m][k] != 10000):
        return dp[m][k]
    r = 0
    for i in li:
        r = max(r,sol2(m-1,k^i))
    dp[m][k] = r
    return r

#print((sol(m,0)))
#dp = [[10000 for i in range(1025)] for i in range(m+1)]
print((sol2(m,0)))