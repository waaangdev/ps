import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

sys.setrecursionlimit(100011)


n = int(sys.stdin.readline())
nodes_c = n
ways_down = [[] for i in range(200010)]
ways_up = [-1 for i in range(200010)]

ways_up_q_sorted = []

ways_up_jump = [-1 for i in range(200010)]
ways_up_jump_c = [0 for i in range(200010)]
ways_up_jump_e = [0 for i in range(200010)]
ways_down_jump = [[] for i in range(200010)]

nodes_jump_btw = [[i] for i in range(200010)]

ways_d = [-1]*200010
ways_d_level = [-1]*200010


d_level = [0]*(200010)
for i in range(len(d_level)):
    for j in range(19,-1,-1):
        if(i%(2**j)==0):
            d_level[i]=j
            break

for i in range(n-1):
    inp = list(map(int,sys.stdin.readline().split()))
    ways_down[inp[0]-1].append([i+1,inp[1],inp[2]])

def treetobin(idx,d,hisl,hisle):
    global nodes_c
    ways_d[idx]=d
    ways_d_level[idx]=d_level[d]

    for i in range(0,ways_d_level[idx]+1):
        hisl[i]=idx
        hisle[i]=0
    #print("dfs",idx,hisl)

    if(ways_d_level[idx]!=19):
        ways_up_jump[idx] = hisl[ways_d_level[idx]+1]
        ways_up_jump_e[idx] = hisle[ways_d_level[idx]+1]
        ways_down_jump[hisl[ways_d_level[idx]+1]].append(idx)

    if(len(ways_down[idx]) > 2):
        #print("aaa")
        ways_down[nodes_c]=(ways_down[idx][1:])

        ways_down[idx] = [ways_down[idx][0],[nodes_c,-1,0]]

        nodes_c+=1

    for i in ways_down[idx]:
        ways_up[i[0]] = idx
        ways_up_q_sorted.append([i[1],i[0]])
        hisle2 = hisle[:]
        for j in range(20):
            hisle2[j]+=i[2]
        treetobin(i[0],d+1,hisl[:],hisle2)

treetobin(0,0,[-1]*20,[0]*20)

ways_up_q_sorted.sort()
#print(ways_up_q_sorted)
#print(ways_up_jump[:nodes_c])
ways_up_q_sorted = deque(ways_up_q_sorted)

node_e_max = [[0]*11 for i in range(nodes_c)]


def nodeEmaxset(idx):
    for i in ways_down[idx]:
        nodeEmaxset(i[0])
        for j in range(1,11):
            node_e_max[idx][j] = max(node_e_max[idx][j],node_e_max[i[0]][j-1]+i[2])


nodeEmaxset(0)

def nodebtwset(idx):
    li =[[] for i in range(20)]
    for i in ways_down[idx]:
        dli = nodebtwset(i[0])
        for j in range(ways_d_level[idx],20):
            li[j]+=dli[j]
            nodes_jump_btw[idx]+=dli[j]

    li[ways_d_level[idx]] = [idx]

    return li

nodebtwset(0)
#print(nodes_jump_btw[:nodes_c])
q = int(sys.stdin.readline())

ql = [list(map(int,sys.stdin.readline().split()))+[i] for i in range(q)]
rl = [-1]*q
ql.sort()

for i in range(q):
    while ways_up_q_sorted:
        qpop = ways_up_q_sorted.popleft()
        if(qpop[0] > ql[i][0]):
            ways_up_q_sorted.appendleft(qpop)
            break
        else:
            #print(qpop)
            idx = qpop[1]

            
            for j in nodes_jump_btw[idx]:
                #print(ways_up_jump[j])
                ways_up_jump_c[j] += 1
                dum = ways_d[j]-ways_d[ways_up_jump[j]]- ways_up_jump_c[j]
                #print(ways_d[j],ways_d[ways_up_jump[j]],ways_up_jump_c[j],dum)
                if(dum < 0):
                    print(0/0)  
                for k in range(11):
                    if(k-dum >= 0):
                        node_e_max[ways_up_jump[j]][k] = max(node_e_max[j][k-dum]+ways_up_jump_e[j],node_e_max[ways_up_jump[j]][k])

            while idx != 0:
                nidx = ways_up_jump[idx]
                #print("nidx",nidx)

                dum = ways_d[idx]-ways_d[nidx]- ways_up_jump_c[idx]
                if(dum < 0):
                    print(0/0)
                #print(dum,ways_up_jump_c[idx])
                for j in range(11):
                    if(j-dum >= 0):
                        #print(j,dum,ways_up_jump_c[idx])
                        node_e_max[nidx][j] = max(node_e_max[idx][j-dum]+ways_up_jump_e[idx],node_e_max[nidx][j])

                idx = nidx
    #print(node_e_max[0])
    rl[ql[i][2]] = node_e_max[0][ql[i][1]]
for i in rl:
    print(i)