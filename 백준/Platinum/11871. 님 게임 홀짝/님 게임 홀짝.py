# #님 게임 홀짝
# grundySU = [0 for i in range(100)]
# grundySU[0] = 0
# grundySU[1] = 1
# grundySU[2] = 0
# for i in range(3,100):
#     r= 0
#     mex = [0 for _ in range(100)]
#     for j in range(2,i,2):
#         mex[grundySU[i-j]] = 1
#     if(i%2 != 0):
#         mex[grundySU[0]] = 1
#     for j in range(100):
#         if(mex[j]):
#             r=j+1
#         else:
#             break
#     grundySU[i] = r
# for i in range(0,100,2):
#     print(i,grundySU[i])
# for i in range(1,100,2):
#     print(i,grundySU[i])
    



n = int(input())
li=list(map(int,input().split()))
xor = 0
for i in range(n):
    if(li[i]%2==0):
        li[i] = li[i]//2-1
    else:
        li[i] = li[i]//2+1
    xor = xor^li[i]
if(xor == 0):
    print("cubelover")
else:
    print("koosaga")
