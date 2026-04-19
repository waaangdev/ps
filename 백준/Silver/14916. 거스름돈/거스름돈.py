import sys
from collections import deque
import math

a = int(sys.stdin.readline().strip())
r = a//5
if(a != 1 and a!=3):
    if((a%5)%2 == 0):
        print(r+(a%5)//2)
    else:
        if((a%5) == 1):
            print(r-1+3)
        elif((a%5) == 3):
            print(r-1+4)
        else:
            print(-1)
else:
    print(-1)