"파티"

import sys
from collections import deque

maul_su,doro_su,end = map(int,sys.stdin.readline().strip().split())
end -=1

doro = [[] for i in range(maul_su)]
doro2 = [[] for i in range(maul_su)]

for i in range(doro_su):
    inp = list(map(int,sys.stdin.readline().strip().split()))
    doro[inp[0]-1].append([inp[1]-1,inp[2]])
    doro2[inp[1]-1].append([inp[0]-1,inp[2]])
    
way = [-1 for i in range(maul_su)]
way[end] = 0

q = [i for i in range(maul_su)]

minq = 0
minq_idx = end
while q:
    
    q_pop = q[minq_idx]
    del q[minq_idx]
    
    for i in range(len(doro[q_pop])):
        if(way[doro[q_pop][i][0]] == -1 or way[doro[q_pop][i][0]] > way[q_pop]+doro[q_pop][i][1]):
            way[doro[q_pop][i][0]] = way[q_pop]+doro[q_pop][i][1]
    
    minq = -1
    minq_idx = 0
    for i in range(len(q)):
        if(way[q[i]] != -1 and (way[q[i]] < minq or minq == -1)):
            minq = way[q[i]]
            minq_idx = i
            




way2 = [-1 for i in range(maul_su)]
way2[end] = 0

q = [i for i in range(maul_su)]

minq = 0
minq_idx = end
while q:
    
    q_pop = q[minq_idx]
    del q[minq_idx]
    
    for i in range(len(doro2[q_pop])):
        if(way2[doro2[q_pop][i][0]] == -1 or way2[doro2[q_pop][i][0]] > way2[q_pop]+doro2[q_pop][i][1]):
            way2[doro2[q_pop][i][0]] = way2[q_pop]+doro2[q_pop][i][1]
    
    minq = -1
    minq_idx = 0
    for i in range(len(q)):
        if(way2[q[i]] != -1 and (way2[q[i]] < minq or minq == -1)):
            minq = way2[q[i]]
            minq_idx = i
            
way3 = [0 for i in range(maul_su)]

for i in range(maul_su):
    way3[i] = way[i] +way2[i] 
print(max(way3))