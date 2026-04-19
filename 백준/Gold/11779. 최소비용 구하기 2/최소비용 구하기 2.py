"최소비용 구하기 2"

import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

way = [[] for i in range(n)]
point = [[-1,[]] for i in range(n)]

for i in range(m):
    inp1,inp2,inp3 = map(int,sys.stdin.readline().split())
    inp1-=1
    inp2-=1

    way[inp1].append([inp2,inp3])

st,end = map(int,sys.stdin.readline().split())
st-=1
end -=1

point[st][1] = [st+1]
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
            point[way[qpop][i][0]][1] = point[qpop][1]+[way[qpop][i][0]+1]

    min_ = -1
    min_index = -1
    for i in range(len(q)):
        if(min_ == -1 or (min_ > point[q[i]][0] and point[q[i]][0] != -1)):
            min_ = point[q[i]][0]
            min_index = i

    if(min_ == -1):break
print(point[end][0])
print(len(point[end][1]))
print(*point[end][1])
