import sys
#n,m=list(map(int,sys.stdin.readline().split()))
# dp = [[-1 for i in range(1048576*2)] for i in range(20)]
# pows = [2**i for i in range(21)]
# def sol(idx,bit):
#     if(idx == n):
#         return 1
#     if(dp[idx][bit+pows[n]]!=-1): return dp[idx][bit+pows[n]]
#     r = 0
#     bit2 = bit
#     for i in range(n):
#         if(bit2%2==0 and i!=idx):
#             r+=sol(idx+1,(bit+pows[i]))
#         bit2//=2
#     dp[idx][bit+pows[n]] = r
#     return r
li = [0,0,1,2,9,44,265,1854,14833,133496,1334961,14684570,176214841,2290792932,32071101049,481066515734,7697064251745,130850092279664,2355301661033953,44750731559645106,895014631192902121]
# for i in range(1,21):
#     n=i
#     print(sol(0,0))
for i in range(int(input())):
    print(li[int(input())])