#숫자 숏코딩
import math

dp = [""]*100000001
dp2 = [0]*100000001

def fun(n):
    if(dp[n] != ""):
        return dp[n]
    if(n<1000):
        dp[n] = str(n)
        dp2[n] = len(dp[n])
        return str(n)
    r = str(n)
    rlen = len(r)

    for i in range(2,n//2):
        if(n%i == 0):
            rdum = fun(i)+" "+fun(n//i)+" *"
            rlendum = dp2[i]+dp2[n//i]+1
            if(rlendum < rlen):
                r = rdum
                rlen=rlendum
    dp[n] = r
    dp2[n] = rlen
    return r

for i in range(2,int(math.sqrt(100000000))):
    for j in range(1,100000000):
        dum = (i ** j)
        #print(i,j)
        if(dum > 100000000):
            break
        if(dum > 1000):
            dum2 = fun(i)+" "+fun(j)+" ^"
            dum2len = len(dum2.replace(" ",""))
            if(dum2len < len(str(dum))):
                if(dp[dum] == "" or dum2len < dp2[dum]):
                    dp[dum] = dum2
                    dp2[dum] = dum2len

#for i in range(1,100001):
#    if(fun(i) != str(i)):
#        print(fun(i),i)
print(fun(int(input())))