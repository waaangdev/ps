from collections import deque
import sys
a,b = map(int,input().split())
ang = [[1,0],[0,1]]
li = []
for i in range(a):
    c = sys.stdin.readline().strip().split()
    for j in range(b):
        if(c[j] == '1'):
            li.append([i,j])
t = 1
me = 0
m = [[0 for i in range(b)] for i in range(a)]
for j in range(len(li)):
    m[li[j][0]][li[j][1]] = 1
while 1:
    t+=1
    li2 = deque([[0,0]])
    while 1:
        lin = len(li2)
        if(lin == 0):
            break
        for j in range(lin):
            for k in range(2):
                for l in range(-1,2,2):
                    if(li2[0][0]+ang[k][0]*l < a and li2[0][0]+ang[k][0]*l >= 0 and li2[0][1]+ang[k][1]*l < b and li2[0][1]+ang[k][1]*l >= 0):
                        if(m[li2[0][0]+ang[k][0]*l][li2[0][1]+ang[k][1]*l] != 1 and m[li2[0][0]+ang[k][0]*l][li2[0][1]+ang[k][1]*l] != t):
                            li2.append([li2[0][0]+ang[k][0]*l,li2[0][1]+ang[k][1]*l])
                            m[li2[0][0]+ang[k][0]*l][li2[0][1]+ang[k][1]*l] = t
            m[li2[0][0]][li2[0][1]] = t
            li2.popleft()
    e = 0
    for j in range(len(li)):
        if(m[li[j][0]][li[j][1]] == 1):
            e+=1
            d = 0
            for k in range(2):
                for l in range(-1,2,2):
                    if(m[li[j][0]+ang[k][0]*l][li[j][1]+ang[k][1]*l] <= t and m[li[j][0]+ang[k][0]*l][li[j][1]+ang[k][1]*l] > 1):
                        d+=1
            if(d < 2):
                m[li[j][0]][li[j][1]] = 1
            else:
                m[li[j][0]][li[j][1]] = -1
    if(e == 0):
        break
    me = e
print(t-2)