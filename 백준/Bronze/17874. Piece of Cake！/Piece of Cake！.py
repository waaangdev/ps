import sys
import math
from collections import deque
import heapq


inp =list(map(int,sys.stdin.readline().strip().split()))
print(max(inp[2],inp[0]-inp[2])*max(inp[1],inp[0]-inp[1])*4)