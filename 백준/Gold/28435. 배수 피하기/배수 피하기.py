import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

for _ in range(1):

    n,k = list(map(int,sys.stdin.readline().split()))
    li = list(map(int,sys.stdin.readline().split()))
    li2 = [0 for i in range(k+1)]

    for i in range(n):
        li2[li[i]%k] += 1
    
    def fastpow(a,n):
        if(n == 0):
            return 1
        if(n==1):
            return a%1000000007
        if(n%2==0):
            return fastpow(a,n//2)**2%1000000007
        else:
            return fastpow(a,n//2)**2*a%1000000007
    #print(li2)



    r = 0
    r2=0
    lic = n
    lic_prev = 0
    # if(li2[k//2] == 1):
    #     lic+=1

    for i in range((k)//2+1):
        if((k)%2 == 0 and i == (k)//2):
            lic-=li2[i]
        else:
            lic-=li2[i]+li2[-i-1]

        dum1 = ((fastpow(2,li2[i])-1)*(fastpow(2,li2[-i-1])-1))%1000000007 #안되는조합갯수
        if(i == 0):
            dum1=(fastpow(2,li2[0])-1-li2[0])
        if((k)%2 == 0 and i == (k)//2):
            dum1 = (fastpow(2,li2[k//2])-1-li2[k//2])

        dum2 = fastpow(2,lic)#남은거걍뽑
        dum3 = (fastpow(2,lic_prev)-r2)#이전꺼로만만든거중안되는거
        r+=(dum1*dum2*dum3)%1000000007
        #print(dum1,dum2,dum3,r2)
        r2=r2*(fastpow(2,li2[i])*fastpow(2,li2[-i-1]))+(dum1*dum3)%1000000007
        

        lic_prev+=li2[i]+li2[-i-1]

        r%=1000000007
        r2%=1000000007


    #print(r)
    r = fastpow(2,n)-1-n-r+1000000007
    r%=1000000007
    print(r)

    # r2 = 0
    # for i in range(2**n):
    #     dum = bin(i)[2:][::-1]+"000000000000000000"
    #     dum2 = 0
    #     li2 = []
    #     for j in range(n):
    #         if(dum[j]=='1'): li2.append(li[j])
    #     if(len(li2) >= 2):
    #         dum2 = 1
    #         for j in range(len(li2)):
    #             for k1 in range(j):
    #                 if((li2[j]+li2[k1]) % k == 0):
    #                     dum2 = 0
    #     #if(dum2==1):print(li2,dum2)
    #     r2+=dum2
    # print(r2)

    # if(r!=r2):
    #     break
    # 4 8
    #     -
    #     5
    #     6
    #     10
    #     5 6
    #     6 10
    #     5 10
    #     5 6 10

    # 6 10
    #     -
    #     4
    #     5
    #     8
    #     4 5
    #     5 8

# 1 6 (2 3 4 5) = 16
# 2 5 (3 4)
#     -
#     1
#     6
#     = 12
# 3 4
#     -
#     1
#     6
#     2
#     5
#     1 2
#     1 5
#     6 2
#     6 5

#     1 6 (2 5)
#     2 5 1
#     2 5 6
#     2 5
#  = 9