import sys
from collections import deque

def find(a):
    b = a
    while 1:
        if(a == bumo[a]):
            break
        c = a
        a = bumo[a]
        bumo[c] = a
    bumo[b] = a
    return a

m_h,m_w = map(int,sys.stdin.readline().split())
m = []
ang = [[0,1],[1,0],[0,-1],[-1,0],[0,0]]

for i in range(m_h):
    m.append([int(i) for i in list(sys.stdin.readline().strip())])

allq = deque([])
count = 3
min_count_bul1 = 0
bul_size = []
for i in range(m_h):
    for j in range(m_w):
        if(m[i][j] == 0):
            m[i][j] = count
            q = deque([[i,j]])
            allq.append([i,j])
            bul_size.append(1)
            min_count_bul1 += 1
            while q:
                qpop = q.popleft()
                for k in range(4):
                    dum1 = qpop[0]+ang[k][0]
                    dum2 = qpop[1]+ang[k][1]
                    if(dum1 < m_h and dum1 > -1 and dum2 < m_w and dum2 > -1):
                        if(m[dum1][dum2] == 0):
                            q.append([dum1,dum2])
                            allq.append([dum1,dum2])
                            m[dum1][dum2] = count
                            bul_size[count-3] += 1
                            min_count_bul1 += 1
            count += 1

count -= 3
bumo = [i for i in range(count)]
bumo_count = [1 for i in range(count)]
br = 0
t = 0
min_count_bul = 0
min_count_t = 0
if(count == 0):
    print(0,0)
elif(count == 1):
    print(0,bul_size[0])
else:
    min_true = False
    while allq:
        t+=1
        for i in range(len(allq)):
            qpop = allq.popleft()
            dum3 = m[qpop[0]][qpop[1]]
            for k in range(4):
                dum1 = qpop[0]+ang[k][0]
                dum2 = qpop[1]+ang[k][1]
                dum7 = find(dum3-3)
                if(dum1 < m_h and dum1 > -1 and dum2 < m_w and dum2 > -1):
                    if(m[dum1][dum2] != 2):
                        for l in range(4):
                            if(l%2 != k%2 or l==k):
                                dum11 = dum1+ang[l][0]
                                dum22 = dum2+ang[l][1]
                                if(dum11 < m_h and dum11 > -1 and dum22 < m_w and dum22 > -1):
                                    dum6 = find(m[dum11][dum22]-3)
                                    if(m[dum11][dum22] > 2 and dum6 != dum7):
                                        dum4 = min(dum6,dum7)
                                        dum5 = max(dum6,dum7)
                                        bumo[dum6] = dum4
                                        bumo[dum7] = dum4
                                        bumo_count[dum4] += bumo_count[dum5]
                                        bul_size[dum4] += bul_size[dum5]
                                        min_true = True
                                        min_count_t = t
                    if(m[dum1][dum2] == 1):
                        allq.append([dum1,dum2])
                        m[dum1][dum2] = dum3
                        bul_size[dum7] += 1
                        min_count_bul1 += 1
        if(min_true):
            min_true = False
            min_count_bul = min_count_bul1

    print(min_count_t,min_count_bul)
