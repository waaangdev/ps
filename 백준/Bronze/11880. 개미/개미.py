import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

11880

import sys
for i in range(int(sys.stdin.readline())):
    a,b,c=map(int,sys.stdin.readline().split())
    
    print(min([a**2+((b+c)**2),c**2+((b+a)**2),b**2+((c+a)**2)]))
