from collections import deque
a,b = map(int,input().split())
m = [[0 for i in range(a)] for i in range(a)]
bi = [deque([]) for i in range(b)]
ang = [[1,0],[0,1]]

for i in range(a):
    c = input().split()
    for j in range(a):
        if(c[j] != '0'):
            bi[int(c[j])-1].append([i,j])
        m[i][j] = int(c[j])
q,w,e = map(int,input().split())
t = 0
while 1:
    if(t == q):
        print(m[w-1][e-1])
        break
    for i in range(b):
        lele = len(bi[i])
        for j in range(lele):
            m[bi[i][0][0]][bi[i][0][1]] = i+1
            for k in range(2):
                for l in range(-1,2,2):
                    if(bi[i][0][0]+ang[k][0]*l > -1 and bi[i][0][0]+ang[k][0]*l < a and bi[i][0][1]+ang[k][1]*l > -1 and bi[i][0][1]+ang[k][1]*l < a):
                        if(m[bi[i][0][0]+ang[k][0]*l][bi[i][0][1]+ang[k][1]*l] == 0):
                            bi[i].append([bi[i][0][0]+ang[k][0]*l,bi[i][0][1]+ang[k][1]*l])
                            m[bi[i][0][0]+ang[k][0]*l][bi[i][0][1]+ang[k][1]*l] = i+1
            bi[i].popleft()
    t+=1