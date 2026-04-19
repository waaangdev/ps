"무엇을 아느냐가 아니라 누구를 아느냐가 문제다"

import sys
from collections import deque

case = int(sys.stdin.readline())

for c in range(case):
    n,m = map(int,sys.stdin.readline().split())
    way = [[] for i in range(m)]
    for i in range(n):
        inp1,inp2,inp3 = map(int,sys.stdin.readline().split())
        way[inp1].append([inp2,inp3])
        way[inp2].append([inp1,inp3])
    
    point = [[-1,[]] for i in range(m)]
    
    q = [i for i in range(m)]
    
    min_ = 0
    min_i = 0
    
    point[min_i][0] = 0
    point[min_i][1] = [0]
    while q:
        qpop = q[min_i]
        del q[min_i]
        
        for i in range(len(way[qpop])):
            if(point[way[qpop][i][0]][0] == -1 or point[way[qpop][i][0]][0] > point[qpop][0]+ way[qpop][i][1]):
                point[way[qpop][i][0]][0] = point[qpop][0]+ way[qpop][i][1]
                point[way[qpop][i][0]][1] = point[qpop][1]+[way[qpop][i][0]]
                
        min_ = -1
        min_i = -1
        
        for i in range(len(q)):
            if(point[q[i]][0] != -1 and (min_ == -1 or point[q[i]][0] < min_)):
                min_ = point[q[i]][0]
                min_i = i
                
        if(min_i == -1): break
    if(point[m-1][1] != []):
        print("Case #"+str(c+1)+":",*point[m-1][1])
    else:
        print("Case #"+str(c+1)+": -1")