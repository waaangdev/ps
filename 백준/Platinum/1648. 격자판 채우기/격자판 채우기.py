n,m = map(int,input().split())
dp = [[-1 for i in range(2**15)] for i in range(n*m)]
def sol(idx,li):
    #print(idx,li)
    if(idx == 0): return int(li[0])
    if(dp[idx][int('0b'+li,2)] != -1): return dp[idx][int('0b'+li,2)]
    r = 0
    dum = '0'
    if(idx <= m):
        dum = '1'
    if(li[0]=='1'):
        r += sol(idx-1,li[1:]+dum)
    if(li[0]=='0'):
        if(li[-1]=='0'):
            r+= sol(idx-1,(li[1:-1])+'1'+dum)
        if(li[1]=='0' and idx%m!=0):
            r += sol(idx-1,'1'+(li[2:])+dum)
    r %= 9901
    dp[idx][int('0b'+li,2)] = r
    return r 
dum  ='0'*(m+1)
if(n==1):
    dum  ='0'*(m)+'1'
print(sol(n*m-1,dum))
# for i in range(n*m):
#     print(dp[i][0])