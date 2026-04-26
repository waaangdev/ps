import sys
from collections import deque
import random
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


for _ in range(int(input())):
    l,r = list(map(int,sys.stdin.readline().split()))
    
    if(l<=r//2+r%2):
        print(r//2+r%2,end=' ')
        a = -1
        for i in range(r,l-1,-1):
            if(i!=r//2+r%2):
                print(i*a,end=' ')
                a*=-1
    else:
        print(l,end=' ')
        a = -1
        for i in range(r,l-1,-1):
            if(i!=l):
                print(i*a,end=' ')
                a*=-1
    print()