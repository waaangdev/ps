
import sys
from collections import deque
import random
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

li="""@   @
@   @
@@@@@
@   @
@@@@@""".split("\n")
n = int(sys.stdin.readline())
for i in range(len(li)*n):
    for j in range(5*n):
        print(li[i//n][j//n],end="")
    print()