import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

#sys.setrecursionlimit(100001)

n = int(sys.stdin.readline())
li = []
st = deque()
c = 1
rl = ''
for i in range(n):
    inp = int(sys.stdin.readline())
    if(c <= inp ):

        while (c <= inp):
            st.append(c)
            rl+='+\n'
            c+=1
        rl+='-\n'
        st.pop()
    elif((st and st.pop() == inp)):
        rl+='-\n'

        pass
    else:
        rl = "NO"
        break
sys.stdout.write(rl)