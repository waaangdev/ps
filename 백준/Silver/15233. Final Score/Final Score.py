import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

a,b,g =  list(map(int,sys.stdin.readline().split()))
li1 = list(sys.stdin.readline().split())
li2 = list(sys.stdin.readline().split())
li3 = list(sys.stdin.readline().split())

sc = 0
for i in li3:
    if(i in li1):
        sc+=1
    if(i in li2):
        sc-=1
if(sc < 0):
    print("B")
elif(sc>0):
    print("A")
else:
    print("TIE")