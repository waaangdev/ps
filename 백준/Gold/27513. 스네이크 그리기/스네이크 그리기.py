import sys
from collections import deque
import math

b,c = map(int,sys.stdin.readline().split())

print(b*c-(b*c %2))

poi = [1,1]
m = 0
m2 = 1
pang= 0
ang = [[0,1],[-1,0],[0,-1],[1,0]]

while 1:
    print(*poi)
    if(m == 0):
        if(m2 == 0):
            poi[1]-=1
            if(poi[1] == 1):
                poi[1]+=1
                poi[0]+=1
                m2 = 1
                if(poi[0] == b):
                    poi[1]-=1
                    m = 2
        elif(m2 == 1):
            poi[1]+=1
            if(poi[1] > c):
                poi[1]-=1
                poi[0]+=1
                m2 = 0
                if(poi[0] == b-1):
                    m = 1
                    m2 = ((b*c %2) == 0)
                if(poi[0] == b):
                    poi[1]+=1
                    m = 3
    elif(m == 1):
        if(m2 == 0):
            poi[1]-=1
            if(poi[1] == 0):
                poi[1]+=1
                if(poi[0] == 1): 
                    break
                m = 2
            m2 = 1
        elif(m2 == 1):
            poi[0]+=1
            m2 = 2
        elif(m2 == 2):
            poi[1]-=1
            m2 = 3
        elif(m2 == 3):
            poi[0]-=1
            m2 = 0
    if(m == 2):
        poi[0]-=1
        if(poi[0] == 1):
            break
    if(m == 3):
        poi[1]-=1
        if(poi[1] == 1):
            m = 2