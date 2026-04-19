n = int(input())
r = (0)
li =list(map(int,input().split()))
dum = 0
dum1 = 0
for i in li:
    r = r^(i)
    if(i==1): dum1+=1
if(r == 0):
    print("cubelover")
else:
    print("koosaga")

# dp = [{},{}]
# def sol(li,turn):
#     if(sum(li)==0):
#         return turn
#     str0 = ''.join(list(map(str,li)))
#     if(str0 in dp[turn]):
#         return dp[turn][str0] 
#     r = 0
#     for i in range(len(li)):
#         tmp  = li[i]
#         li[i] -=1
#         while(li[i] > -1):
#             if(sol(li,1-turn) == turn):
#                 r=1    
#             li[i] -=1
#         li[i] = tmp
#     if(r):
#         dp[turn][str0] = turn
#         return turn
#     else:
#         dp[turn][str0] = 1-turn
#         return 1-turn

# if(sol(li,0) == 1):
#     print("cubelover")
# else:
    
#     print("koosaga")