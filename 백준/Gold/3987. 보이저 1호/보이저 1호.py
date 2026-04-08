import sys
#from collections import deque
n,m1 = map(int,input().split())
ang = [[-1,0],[0,1],[1,0],[0,-1]]
a2 = [1,0,3,2]
a3 = [3,2,1,0]
ml = ['U','R','D','L']
m = []
for i in range(n):
    m.append(sys.stdin.readline().strip())
y,x = map(int,input().split())
mt = 0
ma = 0
for i in range(4):
    pl = [y-1,x-1,i]
    t = 0
    v = 0
    mm = [[100 for j in range(m1)] for i in range(n)]
    if(m[pl[0]][pl[1]] != 'C'):
        while 1:
            pl[0]+=ang[pl[2]%4][0]
            pl[1]+=ang[pl[2]%4][1]
            t+=1
            if(pl[0] < 0 or pl[0] >= n or pl[1] < 0 or pl[1] >= m1):
                break
            if(mm[pl[0]][pl[1]] == pl[2]):
                v = 1
                break
            mm[pl[0]][pl[1]] = int(pl[2])
            if(m[pl[0]][pl[1]] == 'C'):
                break
            if(m[pl[0]][pl[1]] == '/'):
                pl[2] = a2[pl[2]]
            if(m[pl[0]][pl[1]] == "\\"):
                pl[2] = a3[pl[2]]
    if(v == 1):
        ma = i
        break
    if(t > mt):
        mt = t
        ma = i
print(ml[ma])
if(v == 0):print(mt)
else:print('Voyager')