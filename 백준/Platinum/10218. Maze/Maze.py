from collections import deque
import copy

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    map_ = [[] for i in range(n)]
    map2 = [[[[0,0] for k in range(4)] for j in range(m)] for i in range(n)]
    dir = [[0,-1],[0,1],[1,0],[-1,0]]
    bang =[[[set([]) for i in range(m)] for i in range(n)] for i in range(100)]
    li=[]
    for i in range(n):
        map_[i] = input()
        for j in range(m):
            if(map_[i][j] == '.'):
                li.append([i,j])
    
    for i in range(n):
        for j in range(m):
            if(map_[i][j] == "."):
                for k in range(4):
                    dum = [i,j]
                    for l in range(10):
                        dum[0] += dir[k][0]
                        dum[1] += dir[k][1]
                        if(map_[dum[0]][dum[1]] == "#"):
                            dum[0] -= dir[k][0]
                            dum[1] -= dir[k][1]
                            break
                        if(map_[dum[0]][dum[1]] == "O"):
                            dum =-1
                            break
                    map2[i][j][k] = dum
    q = deque([[copy.deepcopy(li),[]]])
    br = 0
    r = 0
    id = 0
    for time in range(10):
        lenq = len(q)
        
        for i in range(lenq):
            leniq = len(q[0][0])
            for dir in range(4):
                dum = []
                dummap = [[0 for i in range(m)] for i in range(n)]
                id += 1
                for j in range(leniq):
                    dum2= map2[q[0][0][j][0]][q[0][0][j][1]][dir]
                    if(dum2 != -1):
                        if(dummap[dum2[0]][dum2[1]] == 0):
                            dum.append(dum2)
                            dummap[dum2[0]][dum2[1]] = 1
                if(len(dum) == 0):
                    br = 1
                    r = q[0][1]+[dir]
                else:
                    dum3 = bang[len(dum)][dum[0][0]][dum[0][1]]
                    for j in dum:
                        dum3 = dum3 & bang[len(dum)][j[0]][j[1]]
                    if(len(dum3) == 0):
                        for j in dum:
                            bang[len(dum)][j[0]][j[1]].add(id)
                        q.append([dum,q[0][1]+[dir]])
                    
            q.popleft()
        if(br):
            break

    if(br == 0):
        print("XHAE")
    else:
        for i in r:
            print("LRDU"[i],end='')
        print()