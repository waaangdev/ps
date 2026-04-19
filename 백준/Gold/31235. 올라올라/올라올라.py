import sys
# from collections import deque
# import heapq
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))+[1000000001]
r = 1
his = li[0]
hisi = 0
for i in range(n+1):
    if(li[i] >= his):
        r = max(r, i-hisi)
        his = li[i]
        hisi = i
sys.stdout.write(str(r))