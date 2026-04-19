import sys
from collections import deque

a = int(sys.stdin.readline())

for i in range(a):
    b = int(sys.stdin.readline())
    b = bin(b)[2:]
    r = 0
    lb= len(b)
    for j in range(lb):
        if(b[j] == '1'):
            r+= pow(3,lb-1-j)
    print(r)