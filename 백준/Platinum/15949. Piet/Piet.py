"개미굴"

import sys
from collections import deque

m_h,m_w = map(int,sys.stdin.readline().split())
ang = [[0,1],[1,0],[0,-1],[-1,0]]

mem = [ [[[-1,0] for _ in range(2)] for _ in range(4)]  for _ in range(m_w*m_h)] 
m_count = [[-1 for _ in range(m_w)] for _ in range(m_h)]
m = [[0 for _ in range(m_w)] for _ in range(m_h)]

for i in range(m_h):
    m[i] = list(sys.stdin.readline())

count = 0
for i in range(m_h):
    for j in range(m_w):
        if(m_count[i][j] == -1):
            m_count[i][j] = count
            
            q = deque([[i,j]])
            dum = m[i][j]
            dum2 = [i,j]
            for k in range(4):
                if(mem[count][k][0][(k%2)*-1+1]*ang[k][(k%2)*-1+1] < dum2[(k%2)*-1+1]*ang[k][(k%2)*-1+1] or mem[count][k][0][0] == -1):
                    for l in range(2):
                        mem[count][k][l] = dum2
                elif(mem[count][k][0][(k%2)*-1+1]*ang[k][(k%2)*-1+1] == dum2[(k%2)*-1+1]*ang[k][(k%2)*-1+1]):
                    for l in range(2):
                        if(mem[count][k][l][(k%2)]*ang[(k+((l*2)-1))%4][(k%2)] < dum2[(k%2)]*ang[(k+((l*2)-1))%4][(k%2)]):
                            mem[count][k][l] = dum2

            while q:
                qpop = q.popleft()
                for k in range(4):
                    if(qpop[0]+ang[k][0] > -1 and qpop[0]+ang[k][0] < m_h and qpop[1]+ang[k][1] > -1 and qpop[1]+ang[k][1] < m_w):
                        if(m[qpop[0]+ang[k][0]][qpop[1]+ang[k][1]] == dum and m_count[qpop[0]+ang[k][0]][qpop[1]+ang[k][1]] == -1):
                            q.append([qpop[0]+ang[k][0],qpop[1]+ang[k][1]])
                            m_count[qpop[0]+ang[k][0]][qpop[1]+ang[k][1]] = count

                            dum2 = [qpop[0]+ang[k][0],qpop[1]+ang[k][1]]
                            for k in range(4):
                                if(mem[count][k][0][(k%2)*-1+1]*ang[k][(k%2)*-1+1] < dum2[(k%2)*-1+1]*ang[k][(k%2)*-1+1] or mem[count][k][0][0] == -1):
                                    for l in range(2):
                                        mem[count][k][l] = dum2
                                elif(mem[count][k][0][(k%2)*-1+1]*ang[k][(k%2)*-1+1] == dum2[(k%2)*-1+1]*ang[k][(k%2)*-1+1]):
                                    for l in range(2):
                                        if(mem[count][k][l][(k%2)]*ang[(k+((l*2)-1))%4][(k%2)] < dum2[(k%2)]*ang[(k+((l*2)-1))%4][(k%2)]):
                                            mem[count][k][l] = dum2

            count += 1

pointer = 0
pointer_ang1 = 0
pointer_ang2 = 0
dum2 = 0
dum3 = 0
br = 1
print(m[0][0],end = '')

while br:
    dum = mem[pointer][pointer_ang1][pointer_ang2]
    if(dum[0]+ang[pointer_ang1][0] > -1 and dum[0]+ang[pointer_ang1][0] < m_h and dum[1]+ang[pointer_ang1][1] > -1 and dum[1]+ang[pointer_ang1][1] < m_w):
        if(m[dum[0]+ang[pointer_ang1][0]][dum[1]+ang[pointer_ang1][1]] != 'X'):
            pointer = m_count[dum[0]+ang[pointer_ang1][0]][dum[1]+ang[pointer_ang1][1]]
            print(m[dum[0]+ang[pointer_ang1][0]][dum[1]+ang[pointer_ang1][1]],end = '')
            dum2 = 0
            dum3 = 0
            
        else:
            if(dum2 == 0):
                pointer_ang2 = pointer_ang2*-1+1
                dum2 = 1
            elif(dum2 == 1):
                pointer_ang1 += 1
                pointer_ang1 = pointer_ang1%4
                dum2 = 0
                dum3 += 1
                if(dum3 == 4):
                    br = 0
    else:
        if(dum2 == 0):
            pointer_ang2 = pointer_ang2*-1+1
            dum2 = 1
        elif(dum2 == 1):
            pointer_ang1 += 1
            pointer_ang1 = pointer_ang1%4
            dum2 = 0
            dum3 += 1
            if(dum3 == 4):
                br = 0
