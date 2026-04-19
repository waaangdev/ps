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


n=int(input())
if(n<=2):
    print("NO")
elif(n%3==0):
    print("YES")
    for i in range(2*n):
        print(i%2+1,i%3+1+(i//6)*3)
elif(n%5 == 0):
    print("YES")
    for i in range(2*n):
        print(i%2+1,[1,3,5,4,2,1,3,2,4,5][i%10]+(i//10)*5)
elif(n%4 == 0):
    print("YES")
    for i in range(2*n):
        print(i%2+1,[1,3,4,2,3,1,2,4][i%8]+(i//8)*4)
else:
    print("YES")
    if(n%3==1):
        for i in range(8):
            print(i%2+1,[1,3,4,2,3,1,2,4][i%8]+(i//8)*4)
        for i in range(8,2*n):
            print(i%2+1,4+(i-8)%3+1+((i-8)//6)*3)
    if(n%3==2):
        for i in range(10):
            print(i%2+1,[1,3,5,4,2,1,3,2,4,5][i%10]+(i//10)*5)
        for i in range(10,2*n):
            print(i%2+1,5+(i-10)%3+1+((i-10)//6)*3)
