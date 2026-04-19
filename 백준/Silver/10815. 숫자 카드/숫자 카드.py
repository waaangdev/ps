import sys
#from collections import deque
a = int(input())
li = sorted(list(map(int,input().split())))
b = int(input())
li2 = list(map(int,input().split()))
for i in range(b):
    c = 0
    d = a-1
    t =0
    if(li[c] == li2[i] or li[d] == li2[i]):
        t = 1
    else:
        while 1:
            e = c+(d-c)//2
            if(li[e] == li2[i]):
                t = 1
                break
            elif(li[e] > li2[i]):
                d = e
            else:
                c = e
            if((d-c) == 1):
                break
                
    print(t,end = ' ')