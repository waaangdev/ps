import sys
from collections import deque
import decimal

poisu,waysu = map(int,sys.stdin.readline().split())
way = [[False for i in range(poisu)] for i in range(poisu)]
point = [0 for i in range(poisu)]
way2 = [decimal.Decimal('0') for i in range(poisu)]
way3 = [0 for i in range(poisu)]
way4 = [0 for i in range(poisu)]
for i in range(waysu):
    inp1,inp2 = map(int,sys.stdin.readline().split())
    inp1-=1
    inp2-=1
    way[inp1][inp2] = True
    way2[inp1] = decimal.Decimal( way2[inp1]+decimal.Decimal('1'))
    way3[inp2] += 1
    
q = deque([0])
point[0] = decimal.Decimal('100')
for ii in range(poisu):
    qpop = ii
    if(way2[qpop] !=decimal.Decimal('0') ):
        dum = decimal.Decimal(point[qpop]/way2[qpop])
        for j in range(poisu):
            if(way[qpop][j]):
                way4[j] += 1
                point[j] += dum
                point[qpop] -= dum

print(max(point))