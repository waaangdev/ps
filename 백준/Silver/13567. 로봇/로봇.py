import sys
#from collections import deque
n,m = list(map(int,input().split()))
ang = [[-1,0],[0,1],[1,0],[0,-1]]
pl = [0,0]
pla = 1
br = -1
for i in range(m):
    a = input().split()
    if(a[0] == 'MOVE'):
        pl[0]-=ang[pla%4][0]*int(a[1])
        pl[1]+=ang[pla%4][1]*int(a[1])
        if(pl[0] > n or pl[0] < 0 or pl[1] > n or pl[1] < 0):
            br = 0
            print(-1)
            break
    if(a[0] == 'TURN'):
        pla += -1+int(a[1])*2
if(br):
    print(pl[1],pl[0])