import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))



a,b = list(map(int,sys.stdin.readline().split()))
c,d=a,b
i=0
while([c,d]!=[a,b] or i==0):
    c,d = d,(c+d)%10
    i+=1
print(i+2)