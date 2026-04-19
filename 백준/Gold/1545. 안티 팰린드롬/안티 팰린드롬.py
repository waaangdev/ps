
import sys
from collections import deque
import random
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
s = sys.stdin.readline().strip()
li = [ord(i) for i in s]
li.sort()
res = 1
for i in range(len(li)//2-1,-1,-1):
    l = i
    r = len(li)-l-1
    if(li[l]==li[r]):
        r2=r
        dum = 0
        while(r2 < len(li)):
            if(li[r]!=li[r2]):
                dum=1
                break
            r2+=1
        if(dum == 0):
            r2=l
            dum = 0
            while(r2 > -1):
                if(li[r]!=li[r2]):
                    dum=1
                    break
                r2-=1
        if(dum == 1):
            li[r],li[r2] = li[r2],li[r]
        else:
            res = -1
if(res!=-1):
    res = ''.join([chr(i) for i in li])
print(res)