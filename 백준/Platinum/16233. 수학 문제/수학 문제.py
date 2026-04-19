import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

def sol(a):
    a2 = [0]+list(map(int,list(str(a))))
    r=0
    if(a%9==0):
        a3=sum(a2)//9
        a4=0
        r=0
        while(a3>0):
            if(a2[-2]!=9):
                a4+=10-a2[-1]
                a2[-1]=0
                a2[-2]+=1
                a3-=1
            else:
                a4+=10-a2[-1]
                a2[-1]=0
                a3-=1
                for i in range(-2,-len(a2),-1):
                    if(a2[i]==9):
                        a2[i]=0
                        a3-=1
                    else:
                        break
        if(a3==0):
            r=1
        
    if(r==0):
        return -1
    else:
        return a+a4
br=0

for i in range(int(sys.stdin.readline())):
    a=int(sys.stdin.readline())
    print(sol(a),end=' ')
