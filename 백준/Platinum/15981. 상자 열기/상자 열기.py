import sys
# from collections import deque
# import heapq
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

n = int(sys.stdin.readline())
a,b = 0,1
for i in range(100):
    a+=1
    b*=2
    if(b>=n):
        print(a)
        break
for i in range(a):
    li = []
    for j in range(n):
        #print(bin(j)[-1:1:-1])
        if((bin(j)[-1:1:-1]+"0"*100)[i] == '0'):
            li+=[j+1]
    print(len(li),*li)