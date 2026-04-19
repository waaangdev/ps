import sys
#from collections import deque
qqq = int(input())
for qwe in range(qqq):
    a = int(sys.stdin.readline())
    li = set(list(map(int,sys.stdin.readline().split())))
    b = int(sys.stdin.readline())
    li2 = list(map(int,sys.stdin.readline().split()))
    for i in range(b):
        t =0
        if(li2[i] in li): t=1
        print(t)