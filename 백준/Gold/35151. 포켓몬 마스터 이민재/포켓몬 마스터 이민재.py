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


for _ in range( int(sys.stdin.readline())):
    r,hp = list(map(int,sys.stdin.readline().split()))
    f = int(sys.stdin.readline())
    dum = 0
    hp2=hp
    while hp!=1:
        hp = max(1,hp-f)
        dum+=1
    li = ['G','YS','','Y']
    li.sort(key= lambda x:len(x))
    li2 = []
    #print(li)
    maxp = 0
    maxp2 =""
    for i in li:
        h = 1/3
        s=1
        if('G' in i):
            s=1.5
        if('Y' in i):
            s=2.5
        fc = 0
        while (min(255,h*r*s) != 255 and max(1,hp2-f*fc) != 1):
            fc+=1
            h = (3*hp2-max(1,hp2-f*fc)*2)/(3*hp2)
        dump = min(255,h*r*s)
        if(i=='Y' and fc==0):
            continue
        li2.append((i+'F'*fc,dump))
    
    print(sorted(li2,key=lambda x:(-x[1],len(x[0])))[0][0]+'C')