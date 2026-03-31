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

def print2(li):
    sys.stdout.write(' '.join(list(map(str,li)))+'\n')
    print()
n,h = map(int,input().split())

if(h > n**2 or h < n*2-1):
    print("impossible")

elif(h==n*2-1):
    print2(list(map(lambda x:x*2-1,list(range(n,0,-1)))))

else:
    idx = n
    dum = 0
    while (dum+(idx*2-1)) < h:
        dum+=idx*2-1
        idx-=1

    idx2 = -1
    #print(dum)
    for i in range(1,idx+1):
        if(dum+(i*2-1) >= h):
            idx2 = i
            dum+=(i*2-1)
            break

    #print(idx2)

    
    impa = 0
    onone = 0
    if(dum > h):

        if(idx2 == 1):
            idx2-=1
            dum-=1
            #크기1짜리 안에넣기
        else:
            onone = 1
            if(idx2 == 2):
                if(idx == 2):
                    #임파?
                    impa = 1
                    pass
                else:
                    impa = 2
                    onone = 0
                    offcups = list(range(1,idx+1))

                    if(idx2 != 0):
                        offcups.remove(idx2)
                    if(onone and idx2!=1):
                        offcups.remove(1)
                    offcups.remove(idx)
                    rl=offcups
                    rl +=list(range(idx+2,n+1))[::-1]
                    if(idx2 != 0):
                        rl+=[idx,idx2,idx+1]
                    if(onone):
                        rl+=[1]
                    print2(map(lambda x: x*2-1,rl[::-1]))
                    
            else:
                idx2-=1
            #크기 1짜리 꺼내기
    

    if(impa==1):
        print("impossible")
    elif(impa==0):
        offcups = list(range(1,idx+1))
        if(idx2 != 0):
            offcups.remove(idx2)
        if(onone and idx2!=1):
            offcups.remove(1)
        rl=offcups
        rl +=list(range(idx+1,n+1))[::-1]
        if(idx2 != 0):
            rl+=[idx2]
        if(onone):
            rl+=[1]
        #print(rl)
        print2(map(lambda x: x*2-1,rl[::-1]))
