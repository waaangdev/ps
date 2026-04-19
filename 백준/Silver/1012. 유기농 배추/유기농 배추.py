from collections import deque
import sys
a = int(input())
ang = [[1,0],[0,1]]
for _ in range(a):
    x,y,b = map(int,input().split())
    m = [[0 for i in range(x)] for j in range(y)]
    for i in range(b):
        c,d = map(int,sys.stdin.readline().strip().split())
        m[d][c] = 1
    s = 0
    for i in range(y):
        for i1 in range(x):
            if (m[i][i1] == 1):
                s+=1
                li2 = deque([[i,i1]])
                m[i][i1] = 0
                while 1:
                    lin = len(li2)
                    if(lin == 0):
                        break
                    for j in range(lin):
                        for k in range(2):
                            for l in range(-1,2,2):
                                duma,dumb = li2[0][0]+ang[k][0]*l,li2[0][1]+ang[k][1]*l
                                if(duma < y and duma >= 0 and dumb < x and dumb >= 0):
                                    if(m[duma][dumb] == 1):
                                        li2.append([duma,dumb])
                                        m[duma][dumb] = 0
                        li2.popleft()
    print(s)