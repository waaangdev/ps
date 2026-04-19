import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n = int(sys.stdin.readline())
li1 = list(map(int,sys.stdin.readline().split()))
if((li1.count(1)-li1.count(2))%3 == 0 and li1.count(1)>=li1.count(2)):
    print("Yes")
else:
    print("No")