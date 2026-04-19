# #님 게임 나누기
# dp = [-1]*1000001
# def sol(n):
#     if(n==0):
#         return 0
#     if(dp[n] != -1):
#         return dp[n]
#     mex = [0 for i in range(n+100)]
#     for i in range(1,n+1):
#         mex[sol(n-i)]=1
#     for i in range(1,n//2+1):
#         xor = 0
#         xor = xor ^ sol(i)
#         xor = xor ^ sol(n-i)
#         #print(n,i,n-i)
#         mex[xor]=1

#     #print(mex)
#     r = 0
#     for i in range(n+101):
#         if(mex[i]):
#             r=i+1
#         else:
#             break
#     dp[n] = r
#     return r


def sol(n):
    if(n%4==0):return n-1
    if(n%4==3):return n+1
    return n

# for i in range(100):
#     print(i,sol(i))
    #if(sol(i)!=i): break
n = int(input())
li=list(map(int,input().split()))
xor = 0
for i in range(n):
    xor = xor^sol(li[i])
if(xor == 0):
    print("cubelover")
else:
    print("koosaga")
