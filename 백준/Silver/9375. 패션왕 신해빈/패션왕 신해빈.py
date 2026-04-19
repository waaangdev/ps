from collections import deque
import sys
a = int(input())
for i in range(a):
    b = int(input())
    if(b == 0):
        print(0)
    elif (b == 1):
        input()
        print(1)
    else:
        li = []
        for i in range(b):
            c,d = sys.stdin.readline().strip().split()
            li.append(d)
        li.sort()
        #print(li)
        e = ''
        ee = 0
        s =1
        for i in range(b):
            if(e == li[i]):
                ee+=1
            else:
                s *= (ee+1)
                ee = 1
                e = li[i]
        s *= (ee+1)
        print(s-1)