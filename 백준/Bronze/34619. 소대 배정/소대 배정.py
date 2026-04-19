import sys
# from collections import deque
# import heapq
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

a,b,n,k = list(map(int,sys.stdin.readline().split()))
k-=1
k //= n
print(k//b+1,k%b+1)