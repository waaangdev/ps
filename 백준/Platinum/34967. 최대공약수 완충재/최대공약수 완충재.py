import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))



# li = [1 for i in range(1000)]
# pri = []
# for i in range(2,6023):
#     if(i%3!=0 and i%5!=0  and i%7!=0  and i%11!=0 ):
#         pri.append(i)
# print(len(pri))
# pri2 = []
# for i in range(len(pri)):
#     pri2.append(pri[i]*pri[::-1][i])
# print(max(pri2)*11)


# 소수1*소수2

# 소수2*소수3

# 소수3*소수4

# 1*2
# 2*3
# 3*5
# 
# .
# 2
# 2*1


#4번
#5000개


li = [99990,999900,9999000]

# 1 X
# 1 100
# 100 2
# 2 101
# 101 3
# 6 5 


dum = 10000
for i in range(dum-1):
    li.append((dum-1-i)*(i+dum))
    li.append((i+dum)*(dum-1-i-1))
#print(li[:10])
print(*li[:int(input())])
# dumli = set()
# for i in range(len(li)-1):
#     dumli.add(math.gcd(li[i],li[i+1]))
    #print(math.gcd(li[i],li[i+1]))
#print(len(dumli),len(li)-1,max(li))