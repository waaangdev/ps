"택배"

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

way = [[] for i in range(n)]
point = [[-1,-1] for i in range(n)]

for i in range(m):
    inp1,inp2,inp3 = map(int,sys.stdin.readline().split())
    inp1-=1
    inp2-=1

    way[inp1].append([inp2,inp3])
    way[inp2].append([inp1,inp3])

for st in range(n):
    
    point = [[-1,-1] for i in range(n)]
    
    point[st][0] = 0

    q = [i for i in range(n)]

    min_ = 0
    min_index = st

    while q:
        qpop = q[min_index]
        del q[min_index]

        for i in range(len(way[qpop])):
            if(point[way[qpop][i][0]][0] > point[qpop][0]+way[qpop][i][1] or point[way[qpop][i][0]][0] == -1):
                point[way[qpop][i][0]][0] = point[qpop][0]+way[qpop][i][1]
                if(point[qpop][1] == -1):
                    point[way[qpop][i][0]][1] = way[qpop][i][0]+1
                else:
                    point[way[qpop][i][0]][1] = point[qpop][1]

        min_ = -1
        min_index = -1
        for i in range(len(q)):
            if(min_ == -1 or (min_ > point[q[i]][0] and point[q[i]][0] != -1)):
                min_ = point[q[i]][0]
                min_index = i

        if(min_ == -1):break
    for i in range(n):
        if(point[i][1] != -1):
            print(point[i][1],end = ' ')
        else:
            print("-",end = ' ')
    print()