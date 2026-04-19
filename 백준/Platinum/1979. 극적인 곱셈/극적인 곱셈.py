# for i in range(1,10):
#     rl = [0]*10
#     for k in range(1,10000000):
#             if(str(k)[-1]+str(k)[:-1] == str(k*i)):
#                 if(rl[int(str(k)[-1])] == 0):
#                     rl[int(str(k)[-1])] = k
#     print(i,rl)
# rl = [[0]*10 for i in range(10)]
# for i in range(1,10):
#     for j in range(1,10):
#         num = str(j)
#         lnum = j
#         lnumhis = 0
#         for _ in range(100000):
#             if(lnum*i+lnumhis == j and lnumhis==0):
#                 rl[i][j] = num
#                 break
#             dum = str(lnum*i+lnumhis)
#             lnum = int(dum[-1])
#             num = str(lnum)+num
#             lnumhis = int(dum)//10
#     print(i,rl[i])
i,j = map(int,input().split())
r = 0
num = str(j)
lnum = j
lnumhis = 0
for _ in range(10000):
    #print(num,lnum,lnumhis)
    if(lnum*i+lnumhis == j and lnum!=0):
        r = num
        break
    dum = str(lnum*i+lnumhis)
    lnum = int(dum[-1])
    num = str(lnum)+num
    lnumhis = int(dum)//10
print(r)