#3165

a,b = input().split()
b=int(b)
a = '0'*(16-len(a))+a
r = []
dp = [[[False for i in range(17)] for i in range(2)] for i in range(17)]
def sol(idx,fit,five):
    if(dp[idx][fit][five]):
        return False
    #print((idx,fit,five))
    global r
    if(idx==len(a)):
        if(five==b and (not fit)):
            return True
        dp[idx][fit][five] = True
        return False
    mins = 0
    if(fit): mins = int(a[idx])
    for i in range(mins,10):
        #print(i)
        if(sol(idx+1,0+(i==mins and fit)*1,five+(i==5))):
            r = [i]+r
            return True
    dp[idx][fit][five] = True
    return False
sol(0,1,0)
dum = 0
for i in range(len(r)):
    if(r[i]!=0):
        dum = 1
    if(dum): print(r[i],end='')