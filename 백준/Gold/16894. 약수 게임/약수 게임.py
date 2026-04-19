import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n = int(sys.stdin.readline())
dum = 0
for i in range(2,int(math.sqrt(n))+2):
    if(n%i == 0 and n!=i):
        dum = i
        break
if(dum == 0):
    print("koosaga")
else:
    n//=dum
    dum = 0
    for i in range(2,int(math.sqrt(n))+2):
        #print(i,n)
        if(n%i == 0 and n!=i):
            dum = i
            break
    if(dum == 0):
        print("cubelover")
    else:
        print("koosaga")