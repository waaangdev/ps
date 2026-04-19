import sys
from collections import deque
import random
import math
import heapq

n = int(sys.stdin.readline())
f = int(sys.stdin.readline())

for i in range(100):
    if (int(str(n)[:-2]+"0"*(2-len(str(i)))+str(i))%f)==0:
        print("0"*(2-len(str(i)))+str(i))
        break
