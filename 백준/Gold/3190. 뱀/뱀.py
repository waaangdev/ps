import sys
a= int(input())
m = [[0 for j in range(a)] for i in range(a)]
m1 = [[0 for j in range(a)] for i in range(a)]

pl = [0,0,1]
ang = [[-1,0],[0,1],[1,0],[0,-1]]
mom = [[0,0]]

b = int(input())
for i in range(b):
    apple = [int(j)-1 for j in input().split()]
    m1[apple[0]][apple[1]] = 1

comm = []
c = int(input())
for i in range(c):
    comm.append(input().split())
t = 0
while 1:
    t+=1
    pl[0] += ang[pl[2]%4][0]
    pl[1] += ang[pl[2]%4][1]
    if(pl[0] < 0 or pl[0] == a or pl[1] < 0 or pl[1] == a or m[pl[0]][pl[1]] == 1):
        break
    else:
        mom.insert(0,[pl[0],pl[1]])
        m[pl[0]][pl[1]] = 1
        if(m1[pl[0]][pl[1]] == 0):
            mom1 = mom.pop()
            m[mom1[0]][mom1[1]] = 0
        m1[pl[0]][pl[1]] = 0
    if(len(comm) != 0):
        if(int(comm[0][0]) == t):
            if(comm[0][1] == 'L'):
                pl[2] -= 1
            if(comm[0][1] == 'D'):
                pl[2] += 1
            del comm[0]

print(t)